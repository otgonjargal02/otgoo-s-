import datetime

# strptime  - str to datetime
# https://www.w3schools.com/python/gloss_python_date_format_codes.asp

#as dt # time, date, datetime
# from datetime import datetime 

# MM/DD/YYY
# DD/MM/YYYY
# DD-MM-YYYY
# DD-MM-YY
# DD-Jun-YY 
# DD-Jun-YY HH:MM

mydate = '2023-09-15'
mydate2 = '17/10/23'


mydate_dt  = datetime.datetime.strptime(mydate, "%Y-%m-%d")
mydate2_dt = datetime.datetime.strptime(mydate2, "%d/%m/%y")
mydate2_dt - mydate_dt


# date
today = datetime.date.today()

print("year =", today.year)
print("month =", today.month)
print("day =", today.day)

d = datetime.date(2019, 4, 13)
t1 = datetime.date(month = 7, year = 2018, day = 12)
t2 = datetime.date(year = 2017, month = 12, day = 23)
type(d)
t3 = t1 - t2
print("t3 =", t3)

timestamp = datetime.date.fromtimestamp(1694854346)
timestamp = datetime.date.fromtimestamp(1694854346+2*24*60*60)
timestamp = datetime.date.fromtimestamp(1)
timestamp = datetime.date.fromtimestamp(1+53*12*30*24*60*60)

# find timestamp of now
dt = datetime.datetime.now() 
ts = datetime.datetime.timestamp(dt)

tod = datetime.datetime.today()
ts = datetime.datetime.timestamp(tod)


# time
a = datetime.time(11, 34, 56, 999)
print("hour        =", a.hour)
print("minute      =", a.minute)
print("second      =", a.second)
print("microsecond =", a.microsecond)

b = datetime.time(11, 34, 56) # time(hour, minute and second)
c = datetime.time(hour = 11, minute = 34, second = 56) # time(hour, minute and second)
d = datetime.time(11, 34, 56, 234566) # time(hour, minute, second, microsecond)


# datetime
b = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380) # datetime(year, month, day, hour, minute, second, microsecond)
print("year =", b.year)
print("month =", b.month)
print("hour =", b.hour)
print("minute =", b.minute)
print("timestamp =", b.timestamp())

t4 = datetime.datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime.datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

# timedelta
t1 = datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = datetime.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
t4_ = t4 + t1

date = datetime.date(2023, 6, 17)  # Replace with your date
new_date = date + datetime.timedelta(days=7)
print(new_date)

mydate = '2017-01-22'
my_dt = datetime.datetime.strptime(mydate, "%Y-%m-%d") # convert string to datetime (strptime)
my_dt2 = datetime.datetime.strptime('2017/01/12', "%Y/%m/%d")
my_dt2 = datetime.datetime.strptime('2017/01/12', "%Y/%d/%m")
my_dt2 = datetime.datetime.strptime('17/01/12', "%d/%y/%m")

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
dt = datetime.datetime.strptime("21/11/06 16:30", "%y/%d/%m %H:%M")

# strftime - datetime to string
now = datetime.datetime.now()

t = now.strftime("%H-%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

# my_dt_str = datetime.date.strftime("%Y/%m/%d") # convert datetime to string (strptime)


# replace string
a = '2017/01/15' # to 2017-01-15
a = a.replace('/','-')