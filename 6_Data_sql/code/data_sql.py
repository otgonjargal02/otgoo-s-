import psycopg2 # pip install psycopg2, sqlalchemy
import pandas as pd

connection = psycopg2.connect(
        user = "postgres",
        password = "postgres",
        host = "localhost", # 198.16.16.01, 127.0.0.1, www.prod.xxxcompany.com/serverdb
        port = "5432",
        database = "first"
    )

cursor = connection.cursor()
cursor.execute("SELECT * from employee;")
record = cursor.fetchall()
# cursor.commit() - must when 

# cursor.execute("Select * FROM mytable LIMIT 0")
colnames = [desc[0] for desc in cursor.description]

df = pd.DataFrame(record)
df.columns = colnames

df.to_csv(r'D:\Documents\python\repo\Introduction_Python\4_Data_sql\data\datacsv.csv')

print("Printing database .............")

print(df)

print("Done!")

cursor.close()
connection.close()


cursor.execute("""CREATE TABLE newtable (
    id integer NOT NULL PRIMARY KEY,
    firstname  text NOT NULL,
    lastname   text,
    citizenId  text,
    age        numeric
);""")

connection.commit()


cursor.execute("""INSERT INTO newtable
(id,firstname,lastname,citizenid,age)
VALUES (1, 'Bat','Zorig', 'UB95',22);""")
connection.commit()


cursor.execute("""delete from employee
where age < 25""")
connection.commit()



cursor.close()
connection.close()





# #copy (SELECT * FROM employee
# where firstname LIKE 'B%')
#   TO 'D:\Documents\python\repo\Introduction_Python\4_Data_sql\data\exported.csv'
#   WITH DELIMITER ','
#   CSV HEADER
# ;

# sql
# psql manual
# psql in terminal
# psql in python
# 
# create table
#
#

# https://www.postgresql.org/docs/current/backup-dump.html
# pg_dump -U postgres -d week4 -t datacsv > datacsv.sql
# psql -U postgres -d week4 < datacsv.sql
