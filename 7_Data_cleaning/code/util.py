# IFS data link. https://data.imf.org/?sk=4c514d48-b6ba-49ed-8ab9-52b0c1a0179b&sid=1409151240976

import pandas as pd 
import numpy as np
from datetime import datetime

def data_prep_long():

    # Task 1
    datapath = '7_Data_cleaning/data/'
    df_ = pd.read_csv(datapath + 'raw/IFS.csv',low_memory=False)
    df_['Country Name'].drop_duplicates().to_csv(datapath + 'raw/countries.csv')
    df_['Indicator Name'].drop_duplicates().to_csv(datapath + 'raw/indicators.csv')

    # count country and indicators 
    len(df_['Country Name'].unique())
    len(df_['Indicator Name'].unique())
 
    # keep countries and indicators in the txt files
    countries = read_txt(datapath + 'raw/countries.txt')
    indicators = read_txt(datapath + 'raw/indicators.txt')
    df = df_ # [df_['Country Name'].isin(countries)]
    df = df[df['Indicator Name'].isin(indicators)]

    # keep only useful columns
    df = df[['Country Name','Indicator Name']].join(df.iloc[:,5:-2])

    df.to_csv(datapath + 'clean/IFS_short.csv',index=False)

def data_prep():
    # Task 2
    datapath = '7_Data_cleaning/data/'
    df = pd.read_csv(datapath + 'clean/IFS_short.csv',low_memory=False)

    # First, use melt to unpivot the period columns into a single 'period' column
    df = pd.melt(df, id_vars=['Country Name', 'Indicator Name'], var_name='period', value_name='value')
    
    # Remove mysterious B symbol by replacing it with NaN 
    # df.iloc[:,2:] = df.iloc[:,2:].replace('B', np.nan, regex=True)
    df['value'] = df['value'].replace('B', np.nan, regex=True)

    # there is different row forthe same variable for different frequencies.
    # It has data only in one in frequency, so just sum to remove duplicate indices
    df = df.groupby(['Country Name','Indicator Name','period']).sum().reset_index()
    
    # Then, pivot the melted DataFrame to have years as columns and indicators as separate columns
    df = df.pivot(index=['Country Name', 'period'], columns='Indicator Name', values='value').reset_index()

    # Task 3
    names = {"Exchange Rates, Domestic Currency per U.S. Dollar, End of Period, Rate":'lcy_usd',
                "Exchange Rates, Domestic Currency per U.S. Dollar, Period Average, Rate":'lcy_usd_avg',
                "Financial, Interest Rates, Lending Rate, Percent per annum":'i_lend',
                "Financial, Interest Rates, Deposit, Percent per annum":'i_depo',
                "Monetary, Broad Money, US Dollars":'m2_usd',
                "Monetary, Broad Money, Domestic Currency":'m2',
                "Monetary, Base Money, US Dollars":'mb'}
    df.rename(columns=names,inplace=True)
    df.rename(columns={'Country Name':'country'},inplace=True)

    # Task 4
    df['lcy_usd'] = df['lcy_usd'].replace(0, np.nan)
    df.iloc[:,2:] = df.iloc[:,2:].apply(pd.to_numeric)
    df['m2_usd_new'] = df['m2']/df['lcy_usd']

    # Task 5 

    i_depo_max = df['i_depo'].max()
    i_lend_max = df['i_lend'].max()
    print("Maximum deposit interest rate is: {:.2f}".format(i_depo_max))
    print("Maximum lending interest rate is: {:.2f}".format(i_lend_max))

    print('The information on maximum deposit rate:')
    print(df[df['i_depo'] == i_depo_max])

    # If deposit rate is above 100, replace it with 100

    print('The information on deposit rate 50+:')
    print(df[df['i_depo'] >50])

    df.loc[df['i_depo'] > 50, 'i_depo'] = 50

    # Task 6

    # separate by frequency
    dfm = df[df['period'].str.contains('M')]
    dfm['period'] = dfm['period'].apply(convert_to_two_digit_month)
    dfm.sort_values(by=["country","period"],inplace=True)

    dfq = df[df['period'].str.contains('Q')]
    dfy = df[df['period'].str.len() == 4]

    dfm.to_csv(datapath + 'clean/dfm.csv',index=False)
    dfq.to_csv(datapath + 'clean/dfq.csv',index=False)
    dfy.to_csv(datapath + 'clean/dfy.csv',index=False)


def read_txt(file_name):
    my_list = [line.strip() for line in open(file_name, "r")]
    return my_list

def convert_to_two_digit_month(date_str):
    date_obj = datetime.strptime(date_str, "%YM%m")
    new_date_str = date_obj.strftime("%YM%m")
    return new_date_str


if __name__ ==  "__main__":
    data_prep_long() # may uncomment just to create IFS_short.csv from the original IFS.csv once
    data_prep()
    # pass