# https://www.datacamp.com/community/tutorials/joining-dataframes-pandas?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034364&utm_targetid=aud-438999696719:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1010217&gclid=Cj0KCQjw-4SLBhCVARIsACrhWLUazS1nYmklEry5bfhtoZVfiL4sUI16ghi9Q8bhKYRI_BncYde42DUaAjpHEALw_wcB

import os 
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# working directory
wd = r'D:\\Documents\python\repo\Introduction_Python\2_Data_and_Control_Flow\data'
os.chdir(wd) # set working directory to wd


# import data files
df_ind   = pd.read_excel('data_more.xlsx', sheet_name='loan_ind', 
    usecols='D:I,L',skiprows=6, header=0)

df_corp  = pd.read_excel('data_more.xlsx', sheet_name='loan_corp',
    usecols='C:F',skiprows=3) # header=0. If not header, header=None

# See columns of df_corp which are in Mongolian
df_corp.columns
df_ind.columns

# Change column names of df_corp to the same names in loan_ind

# column by column
# df_corp.rename(columns={'Харилцагчийн дугаар': 'clientId'}, inplace=True)

# multiple columns
df_corp.rename(columns={'Харилцагчийн дугаар': 'clientId',
                   'Зээлийн статус':'loanStatus'},
                   inplace=True)

# rename columns altogether
df_corp.columns = ['clientId','loanAmount','issueDate','loanStatus']


# loan status of df_corp is not uniform and in Mongolian
df_ind['loanStatus']           # see statuses in loan_ind
df_ind['loanStatus'].unique()  # unique status values
df_corp['loanStatus']          # see statuses in loan_corp
df_corp['loanStatus'].unique() # unique status values

# change to usual format for some of df_corp['loanStatus']

# 'эргэлзээт' to 'эргэлзээтэй'
df_corp.loc[df_corp['loanStatus'] == 'эргэлзээт','loanStatus'] = 'эргэлзээтэй'
# 'Хэвийн' to 'хэвийн'
df_corp.loc[df_corp['loanStatus'] == 'Хэвийн','loanStatus'] = 'хэвийн'


# en-mn translation of status   
status_map = dict(zip(['хэвийн','муу','хугацаа хэтэрсэн',
                              'эргэлзээтэй', 'хэвийн бус'],
                      ['norm', 'bad', 'ovrd', 'doub', 'subs']))
       
     
df_corp['loanStatus_en'] = df_corp['loanStatus'].map(status_map)      # status in en
df_corp.drop('loanStatus',axis=1,inplace=True)                        # drop status mn
df_corp.rename(columns={'loanStatus_en': 'loanStatus'}, inplace=True) # rename to 


# Combining dataframes

# Concatenate - zalgah
df_con = pd.concat([df_ind, df_corp],ignore_index=True) 
pd.concat([df_ind, df_corp],keys=['ind', 'corp']) # you know the source 
pd.concat([df_ind, df_corp],keys=['ind', 'corp']).reset_index() # source in column


# Merge (join) - like SQL JOIN
df_in = pd.merge(df_ind, df_corp,on='clientId')             # inner join, by default
df_ou = pd.merge(df_ind, df_corp,on='clientId',how='outer') # outer join
df_le = pd.merge(df_ind, df_corp,on='clientId',how='left')  # left join
df_ri = pd.merge(df_ind, df_corp,on='clientId',how='right') # right join

# clients with individual loans also having corp loan
df_corp.rename(columns={'clientId': 'userId'}, inplace=True) # rename temporarily
pd.merge(df_ind, df_corp,left_on='clientId', right_on = 'userId',
         how='left',suffixes=("_ind","_corp"))  # left join


