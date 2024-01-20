import pandas as pd
import sys 
sys.path.append("D:\\Documents\\python\\repo\\Introduction_Python\\7_Data_cleaning\code")
import util
import plotly.express as px

datapath = '7_Data_cleaning/data/'
df = pd.read_csv(datapath + 'clean/dfy.csv')

# df = df[['country','period','i_depo']]
# df.pivot(index=['country'], columns='period', values='i_depo').reset_index().to_csv(datapath + 'clean/i_depo.csv')
dfp = df.pivot(index=['country'], columns='period', values='i_depo').reset_index()
dfp = dfp.iloc[:,-24:-1]
dfp['i_depo_avg'] = dfp[dfp > 0].mean(axis=1)

dfp.to_csv(datapath + 'clean/i_depo_analysis.csv')

Financial, Interest Rates, Savings Rate, Percent per annum
Financial, Interest Rates, Lending Rate, Percent per annum

Financial, Interest Rates, Lending Rate, Foreign Currency, Euro, Percent per Annum
Financial, Interest Rates, Deposit Rate, Foreign Currency, US Dollar, Percent per Annum
Financial, Interest Rates, Lending Rate, Foreign Currency, US Dollar, Percent per Annum

