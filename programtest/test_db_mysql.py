#!/usr/bin/env python3
import mysql.connector

"""
    descr:mysql 免费开源服务器端数据库，支持高并发
"""
# con1 = mysql.connector.connect(user='root', password='123xxx45', database='test', use_unicode=True)
# cursor1 = con1.cursor()
# cursor1.execute("create table user(id varchar(2) comment '代理主键' PRIMARY KEY ,name varchar(20)  comment '姓名')")
# cursor1.execute("insert into user values ('1','测试名称1')")
# cursor1.execute("insert into user values ('2','测试名称2')")
# cursor1.execute("insert into user values ('3','测试名称3')")
# cursor1.execute("insert into user values ('4','测试名称4')")
# print("cursor1.rowcount:", cursor1.rowcount)
# cursor1.close()
# con1.commit()
# con1.close();

con1 = mysql.connector.connect(user='root', password='123xxx45', database='test', use_unicode=True)
cursor1 = con1.cursor();
cursor1.execute("select * from user where id = %s", ('1',))
values = cursor1.fetchall()
print("values:", values)
cursor1.execute("select * from user")
values = cursor1.fetchall()
print("values:", values)
cursor1.close()
con1.close()
