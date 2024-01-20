# Control Flow
# https://www.programiz.com/python-programming/if-elif-else

import numpy as np
import pandas as pd


# if

# if True|False:
#     do something

num = 3

# >, <, >=, <=, ==, !=, a in list
# and, or
if num > 0:
    print(num, "is a positive number.")

num = -3
if num > 0:
    print(num, "is a positive number.")

if True:
    print(num, "is a positive number.")

if False:
    print(num, "is a positive number.")


if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")


if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
elif num == 1:
    print("One")
else:
    print("Negative number")

# first valid and stop
num = 1
if num > 0:  #1
    print("Positive number")
elif num == 0:
    print("Zero")
elif num == 1:
    print("One")
else:
    print("Negative number")

# nested ifs
num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

### LOOP
### FOR

# for x in range(15):
#     print(x)

for i in range(15):
    print(i, " number")

mylist = ['Bat','Gerel','Bold']

for name in mylist:
    print(name)

# external data
df = pd.read_excel("5_Flow_control/data/data.xlsx")

for row in df.iterrows():
   print(row[1])
   print("row finished----------------")

data_list = []
for index, row in df.iterrows():
   # print(row['firstName'], row['lastName'])
   print("{} and {}".format(row['firstName'], row['lastName']))
   data_list.append([row['firstName'], row['lastName']])

df_list = pd.DataFrame(data_list,columns=['First Name','Last Name'])


for colname in df.columns:
    print(colname)
    # print(df[colname])

# column loop
for name, values in df.iteritems():
    print('{name}: {value}'.format(name=name, value=values[1]))

for column in df:
    print(column)

# break, continue, pass

for i in range(20):
    if i < 13: 
        if np.mod(i,2) == 0:
            print(i, 'Even')
        else:
            print(i, 'Odd')
    else:
        print('Larger than 12:', i)
        break # skip the rest

for i in range(15):
    if (i > 8) & (i < 12): # and = & or = |
        print(i, 'skipping')
        continue # skip this time
    else:
        if np.mod(i,2) == 0:
            print(i, 'Even')
        else:
            print(i, 'Odd')    

    print("Came here because didn't touch the continue part")


for i in range(15):

    if (i < 5) | (i > 8): # | (i < 11): # or = |
        print(i, 'skipping')
        continue # skip this time
    else:
        if np.mod(i,2) == 0:
            print(i, 'Even')
        else:
            print(i, 'Odd') 

    print('The number is either between 5 and 8!')


for i in range(15):  
    if i < 10 :
        # print('developing ...')
        pass
    else:
        print("hi")


mylist = [5.2,10,45,"Bold",54,47,'Chimeg','15']

for item in mylist:
    if isinstance(item, str):  #    type(item) == str
        print(item)

list_float = []
for item in mylist:
    if isinstance(item, float):  # int, str, float
        list_float.append(item)

short_list_int = []
for item in mylist:
    if isinstance(item, int):
        short_list_int.append(item)
                
for item in mylist:
    if type(item) == int:
        print(item)
        
short_list = [1,2,5,15]

for i in range(10):
    if i in short_list:
        print(i)

# WHILE

# infinite loop
i = 1
while i>0:
    print(i)
    
i = 1    
while i < 100:
    print(i)
    i += 1 # i = i + 1
    
i = 1    
while i < 100:
    print(i)
    i *= 2
    
i = 100   
while i > 1:
    print(i)
    i /= 2


i = 100    
while i > 1:
    print(i)
    i -= 2
