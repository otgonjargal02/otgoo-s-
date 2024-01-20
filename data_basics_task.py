#1-р даалгавар
list = [10, 15, 20, 31.5, 'otgoo', 'bayaraa']
list
list.append('dorj')
list
list.pop(3)
list
list.insert(0,'anu')
list
type(list)
del list[1:5]
"ƒ".join(list)
#2-р даалгавар
import datetime

date = '2024.01.20'
date_dt = datetime.datetime.strptime(date,"%Y.%m.%d")
date_dt
string_format = date_dt.strftime("%Y/%m/%d")
print("strdate is = ",string_format)
#3-р даалгавар
table = {"name": "otgoo", "age":25,"hobby":"c"} 
type(table)
table["name"]

