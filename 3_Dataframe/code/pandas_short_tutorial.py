import os 
import pandas as pd

# working directory
wd = r'D:\\Documents\python\repo\Introduction_Python\2_Data_and_Control_Flow\data'
os.chdir(wd) # set working directory to wd


# import data files
df_main = pd.read_excel('data_short_tutorial.xlsx', sheet_name='үндсэн')
df_oth  = pd.read_excel('data_short_tutorial.xlsx', sheet_name='бусад')

df_main.columns
df_oth.columns

# column by column
df_oth.rename(columns={'Утас': 'Утасны дугаар'}, inplace=True)
df_oth['Мэргэжил'].unique()           
       
# Concatenate - zalgah
df_con = pd.concat([df_main, df_oth],ignore_index=True) 
pd.concat([df_main, df_oth],keys=['ind', 'corp']) 
pd.concat([df_main, df_oth],keys=['ind', 'corp']).reset_index()

# Merge (join) - like SQL JOIN
df_in = pd.merge(df_main, df_oth,on='Утасны дугаар')             # inner join, by default
df_ou = pd.merge(df_main, df_oth,on='Утасны дугаар',how='outer') # outer join
df_le = pd.merge(df_main, df_oth,on='Утасны дугаар',how='left')  # left join
df_ri = pd.merge(df_main, df_oth,on='Утасны дугаар',how='right') # right join

# clients with individual loans also having corp loan
df_oth.rename(columns={'Утасны дугаар': 'Утас'}, inplace=True)
pd.merge(df_main, df_oth,left_on='Утасны дугаар', right_on = 'Утас',
         how='left',suffixes=("_ind","_corp"))  # left join


