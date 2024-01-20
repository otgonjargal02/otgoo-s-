import pandas as pd

datapath = "7_Data_cleaning/data/"
df_emp = pd.read_excel(datapath + "raw/employee202309.xlsx")
df2308 = pd.read_excel(datapath + "raw/loan202308.xlsx")
df2309 = pd.read_excel(datapath + "raw/loan202309.xlsx")
df_capital = pd.read_excel(datapath + "raw/capital.xlsx")

# task 1

removelist = [4573102082, 3010183726, 8486314520, 1805775803, 2533347822, 3982958478]
df_emp = df_emp[~df_emp['citizenID'].isin(removelist)]

# task 2
df_emp = df_emp.merge(df2308, on="citizenID",how="left")
df_emp = df_emp.merge(df2309, on="citizenID",how="left",suffixes=("_old","_new"))

df_capital['emp_ratio'] = df_emp[["amount_old","amount_new"]].sum().values / df_capital["capital"].values

# task 3
df_emp.pivot_table(index=['status_old'], columns='status_new', values='amount_old')
df_emp.pivot_table(index=['status_old'], columns='status_new', values='amount_new')


df_emp.to_excel(datapath + "clean/employee.xlsx")
df_capital.to_excel(datapath + "clean/capital.xlsx")

