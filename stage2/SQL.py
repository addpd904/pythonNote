# base>table>data
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql
from pymysql import Connection #a Class
# generate a connection object
# 一、
con_data = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)
# print information of database
print(con_data.get_server_info())

# get cursor object
cursor = con_data.cursor()
# 二、execute the sql statement
# a.select the database
con_data.select_db("campus")
# b.execute the sql statement
# 1.basic grammer
#cursor.execute("create table mytable (id int,name varchar(10))")

# 2.query statement
cursor.execute("select * from student1")
res :tuple=cursor.fetchall()
print(res)

# 3. insert statement
cursor.execute("insert into student1 values (1,'ls','en',100)")
# commit modify
con_data.commit()
# auto commit
# con_data = Connection(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="123456",
#     autocommit=True
# )
con_data.close()