import pandas as pd
import sys 
sys.path.append("D:\\Documents\\python\\repo\\Introduction_Python\\7_Data_cleaning\code")
import util
import plotly.express as px

# Task 7
datapath = '7_Data_cleaning/data/'
df = pd.read_csv(datapath + 'clean/dfm.csv')
df["year"] = pd.to_datetime(df["period"], format='%YM%m').dt.year # create a year column

# yearly average deposit rate
df['i_depo_y'] = df.groupby(["country","year"])["i_depo"].transform('mean')
df_i_depo_y = df.groupby(["country","year"])["i_depo"].mean().reset_index()

# check - import yearly data
dfy = pd.read_csv(datapath + 'clean/dfy.csv')

dfy = dfy.merge(df_i_depo_y,left_on=["country","period"],right_on=["country","year"],how="left",suffixes=('', '_avg'))
dfy["diff_depo"] = dfy["i_depo_avg"] - dfy["i_depo"]


dfy.sort_values(by="diff_depo")    
df[(df["country"]=="Mongolia") & (df["year"]==1992)]


# Task 8

my_var = "i_lend"
# Create a line plot for each country
fig = px.line(df, x='period', y=my_var, color='country', markers=True, line_shape="linear")

# Customize the plot
fig.update_layout(
    title="Monthly Deposit Interest Rate by Country",
    xaxis_title="Date",
    yaxis_title="Value",
)

# Show the plot
fig.show()
