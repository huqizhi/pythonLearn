#!/usr/bin/env python3
import sqlite3

"""
    descr:sqlite3 微型数据库,适用于桌面或者APP等客户端，支持嵌入式
"""
con1 = sqlite3.connect("test.db")
cursor1 = con1.cursor()
# cursor1.execute("create table user(id varchar(20) PRIMARY KEY ,name varchar(20))")
cursor1.execute("INSERT INTO user VALUES ('3','测试名称3')")
print("cursor1.rowcount:", cursor1.rowcount)
cursor1.close()
con1.commit()
con1.close();

con1 = sqlite3.connect("test.db")
cursor1 = con1.cursor();
cursor1.execute("SELECT * FROM user WHERE id = ?", ('1',))
values = cursor1.fetchall()
print("values:", values)
cursor1.execute("SELECT * FROM user")
values = cursor1.fetchall()
print("values:", values)
cursor1.close()
con1.close()
