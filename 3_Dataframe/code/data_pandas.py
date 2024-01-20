# add row sum
# add column sum
# unique


# Pandas
import pandas as pd
import numpy as np

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000) 

# Pandas read examples:
# https://www.datacamp.com/community/tutorials/importing-data-into-pandas

# be careful with backward slash \


# long
df = pd.read_excel("3_Data_table\data\data.xlsx")

# short
import os
os.getcwd() # get current working directory 
os.chdir(r'3_Data_table')
df = pd.read_excel("data\data.xlsx") # //

df.info()
df.dtypes
df.head() # first 
df.tail() # last # df.tail(3)

df.describe() # descriptive statis

df.columns
df.index
df['age']
df.age
df['firstName'] # get firstname of all users
df[['age','firstName']] 

# slicing
# iloc
df.iloc[2,1]
df.iloc[2:5,1:3]

# loc - index
df.loc[5,"lastName"]
df.loc[5:8,"lastName"]
df.loc[5:8,["lastName","firstName"]] #df.loc[5:8,("lastName","firstName")]

df.set_index('firstName') 
new_df = df.set_index('firstName',drop=False)
df.set_index('firstName',drop=False,inplace=True)
# df.index = df['firstName']
df.loc["Gerel","lastName"]
df.loc[["Gerel","Saran"],["lastName","firstName"]]


# filter
df[df['age']<27] 
df[~(df['age']<27)] # >= 27
df[~(df['age']<27)]['age']
df[df["age"]<27][["firstName","lastName","salary","age"]] # df[df["age"]<27]["firstName","lastName","salary","age"]
df[df["age"]>=27][["firstName","lastName","salary","age"]]


df[(df["age"]<27) & (df["salary"]<2.0) & (df["gender"] != "M")][['age','salary','gender']]
df[(df["age"]<27) & (df["salary"]<2.0) & (df["gender"] == "F")][['age','salary','gender']]

# pivot

df.groupby('gender')['salary'].mean()
df.groupby("gender")['salary'].max()
df.groupby("gender")['salary'].min()

df.groupby(['gender','politicalView'])['age'].mean()


df.groupby(['gender','politicalView'])['age'].mean()
df.groupby(['gender','politicalView'])[['age','salary']].mean()
df.groupby(['gender','politicalView'])[['age','salary']].max()

# df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})
res = df.groupby(['gender','politicalView']).agg({'age': ["mean","max"], 'salary': ["max","count"]})

res = df.groupby(['gender','politicalView']) \
        .agg({'age': ["mean","max"], 'salary': ["max","count"]})
res.columns
len(res.columns)
res[('age','mean')]
res['age']
res.columns = ['agemax','agemean','salmax','salcount']
res.index = ['fleft','fright','mleft','mright']
res.index
res.reset_index(inplace=True)


# pivot table 
table = pd.pivot_table(df, values=['age','salary'], index=['gender'],
                    columns=['politicalView'], aggfunc=np.mean)
print(table)
table.to_excel('./result/pivot.xlsx')
table.to_csv('./result/pivot.csv')
table.to_latex('./result/pivot.tex')


table = pd.pivot_table(df, values=['age','salary'], index=['gender', 'politicalView'],
                    aggfunc=np.mean)

# sort
df = df.sort_values(by="yearsInCompany", ascending=False)
df.sort_values(by="yearsInCompany",inplace=True)

df.sort_values(by="gender", inplace=True)
df.sort_values(by=["gender","age"], inplace=True)

# adding a column
df["random_num"] = np.arange(10)
df
del df["random_num"]

# statistics and values
df['age'].mean()
df['age'].sum()
df['age'].max()
df['age'].min()
df['gender'].unique() # array with unique elements
df['politicalView'].unique() # array with unique elements
df.values

# generate data
df = pd.DataFrame()
df["first"] = []
df["second"] = []
df.loc[0] = ["Bat",15]
df.loc[1] = ["Suren",15]


data = {'Name': [], 'Age': []} 
df = pd.DataFrame(data) 
df.loc[0] = ["Bat",15]
df.loc[1] = ["Bat",15]

df = pd.DataFrame(columns=['name', 'age']) 
df.loc[0] = ["Bat",15]
df.loc[1] = ["Bat",15]

list = [['Bat',15],['Tseren',23]]
df = pd.DataFrame(list, columns=['name', 'age'])
df = pd.DataFrame(list, columns=['name', 'age'], index=['first','second']) 

data = {'Name': ['Ba','Be','Bo'], 'Age': [15, 20, 30]} 
df = pd.DataFrame(data) 


# type conversion
data = {'Salary':[1000, 2222, 3321, 4414, 5151],
       'Name': ['Pete', 'Steve',
                   'Brian',
                   'Ryan', 'Jim'],
       'Share':[29.88, 19.05, 8.17,
               7.3, 6.15],
       'Date':['11/24/2020', '12/21/2019', 
               '10/14/2018', '12/13/2017', '01/08/2017'],
       'Date2': [20120902, 20130413, 20140921, 20140321,
                20140321]}
df = pd.DataFrame(data)
df.info()
df['Date'] = pd.to_datetime(df['Date'])
df.info()
df['Date2'] = pd.to_datetime(df['Date2'])
df['Date2'] = pd.to_datetime(df['Date2'],format="%Y%m%d")

# change column name
list = [['Bat',15],['Tseren',23]]
df = pd.DataFrame(list, columns=['name', 'age'])

df.rename(columns={'name': 'Name'}, inplace=True)

df.rename(columns={'Name': 'Ner', 'age': 'Nas'}, inplace=True)
df.columns = ["Нэрс","Нас"]


# saving to files
df.to_csv('./result/my.csv',encoding='utf-8-sig')
df.to_json('./result/my.json', indent=4,force_ascii=False)
df.to_excel('./result/my.xlsx')
df.to_latex('./result/my.tex')
