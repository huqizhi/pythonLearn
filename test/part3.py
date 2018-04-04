#!/usr/bin/env python3
"""
    descr:基本数据类型--Number（数字）、String（字符串）、List（列表）、Tuple（元组）、Sets（集合）、Dictionary（字典）
"""

import io

"""
    descr:变量
        Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
        在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
"""
counter = 100  # 整形
price = 168.99  # 浮点型
name = "runoob"  # 字符串
print(counter)
print(price)
print(name)
# 多变量赋值
a = b = c = 1
print(a)
print(b)
print(c)
a, b, c = 1, 3.14, "yes"
print(a)
print(b)
print(c)

"""
    descr:标准数据类型--Number（数字）：整型、浮点型、布尔型、复数
        type 主要用于判断未知数据类型，isinstance 主要用于判断 A 类是否继承于 B 类
"""
a, b, c, d = 1, 9.8, True, 4 + 3j
print(a)
print(b)
print(c)
print(d)
#  用isinstance判断类型，用type() 函数可以用来查询变量所指的对象类型
print(isinstance(a, int))
print(isinstance(b, int))
print(isinstance(b, float))
print(type(c))
print(type(d))


#  isinstance和type区别在于：type()不会认为子类是一种父类类型；isinstance()会认为子类是一种父类类型；


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # returns True
print(type(A()) == A)  # returns True
print(isinstance(B(), A))  # returns True
print(type(B()) == A)  # returns False
#  删除变量,删除后再读取会报错
del a, b, c, d
#  print(a)
#  数值运算
print(3 + 4)  # 加法
print(5 - 8)  # 减法
print(6 * 6)  # 乘法
print(12 / 5)  # 除法,得到一个浮点数
print(12 // 5)  # 除法，得到一个整形数
print(12 % 9)  # 取余
print(2 ** 5)  # 乘方

"""
    descr:标准数据类型--String(字符串)：python没有字符型，字符是程度为1的字符串
"""
str = "学习是一种信仰"
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到最后一个字符串，但不包含最后一个
print(str[0])  # 输出第一个字符
print(str[2:5])  # 输出第三个字符到第六个字符，但不包含第六个字符
print(str[2:])  # 输出第三个字符到结尾所有字符
print(str * 3)  # 连续输出3次
print(str + "。")  # 连接字符串
print(str + "\n," + "学习是一种享受。")  # 反斜杠\转义特殊字符
print(str + r"\n," + "学习是一种享受。")  # 不想让反斜杠\发生转移，在字符串前加r
str = "sss"
print(str + r"\n," + "学习是一种享受。")  # Python中的字符串可改变，
# str[0] = "a"  # Python字符串中的字符不能改变。

"""
    descr:标准数据类型--List（列表）
"""
list = [32, 8.5, "price", 8 + 5j, [1, 2, 3], ]
tinylist = [45, 82, 3 + 5j]
print(list)  # 输出列表
print(list[2])  # 输出第3个元素
print(list[0:4])  # 输出第1到5间的元素，包括1不包括5
print(list[2:])  # 输出从第3个开始的所有元素
print(tinylist * 2)  # 输出列表连续两次
print(list + tinylist)  # 列表连接后输出
tinylist = [4, 9]  # 列表可改变
print(tinylist)
tinylist[0] = 100  # 列表元素也可以改变
print(tinylist)
#  内置函数
list.append(4 + 4j)  # 向尾部添加单个元素
print(list)
print(list.pop(-1))  # 取出最后元素
print(list)
print(list.pop(1))  # 取出第2个元素
print(list)

"""
    descr:Tuple（元组）
        元组元素不可改变，但它可以包含可变的对象，比如list列表。
        构造包含 0 个或 1 个元素的元组比较特殊
"""
tuple = (36, 52.0, "菏泽", 3 + 9j, -20, "世界很美好", "我想去看看")
tinytuple = (2, 8, "定律")
print(tuple)  # 输出元组
print(tuple[2])  # 输出元组第三个元素
print(tuple[2:5])  # 输出元组第三个到第六个元素间的所有元素，包括头不包括尾
print(tuple[2:])  # 输出元组第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 元组连接并输出
#  元组元素不可改变，但是可以包含可变的元素，例如list
# tuple[0] = 37 ; print(tuple[0])
t = (32, "时间", [3, 2, 7, 6, 8])
t[2].append(16)
t[2][0] = -3
print(t)
#  构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则
tup1 = ()
tup2 = (2,)
print(tup1, tup2)

"""
    descr:Set（集合）
        集合（set）是一个无序不重复元素的序列。
        基本功能是进行成员关系测试和删除重复元素。
        可以使用大括号 { } 或者 set() 函数创建集合，但创建一个空集合必须用 set()
"""
params = {1, 3, 2, 6, 5, 8, 3, 9, 0}
print(params)  # 输出集合自动去重
#  成员测试
if 1 in params:
    print("1在集合中")
else:
    print("1不在集合中")
# 集合运算
a = set("sdfsabiewo")
b = set("dseiopnmnxwerk")
print(a)
print(b)
print(a - b)  # 差集
print(a | b)  # 并集
print(a & b)  # 交集
print(a ^ b)  # 不同时存在的元素

"""
    descr:Dictionary（字典）
        列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
        字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
        键(key)必须使用不可变类型。
        在同一个字典中，键(key)必须是唯一的。
"""
dict = {}  # 初始化空字典
dict["one"] = "python 学习"
dict[2] = "啥也不说啦"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict)  # 输出完整的字典
print(dict["one"])  # 输出键为“one”的值
print(dict[2])  # 输出键为2的值
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
# 构造函数 dict() 可以直接从键值对序列中构建字典
# dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]) #运行出错
# print(dict1)
dict2 = {x: x ** 2 for x in (2, 4, 6)}
print(dict2)
# dict3 = dict(Runoob=1, Google=2, Taobao=3) # 运行出错
# print(dict3)
dict4 = {}
print(type(dict4))
# print(dict({('a', 1), ('b', 2), ('c', 3)}))  # 字典用元组的集合初始化失败
# print(dict([('a', 1), ('b', 2), ('c', 3)])) # 字典用元组的列表初始化失败
# print(dict((('a', 1), ('b', 2), ('c', 3))))  # 字典用元组的元组初始化失败
# print(dict([['a', 1], ['b', 2], ['c', 3]]))  # 字典用列表的列表初始化失败
# print(dict({['a', 1], ['b', 2], ['c', 3]}))  # 字典用列表的集合初始化失败
# print(dict((['a', 1], ['b', 2], ['c', 3])))  # 字典用列表的元组初始化失败
print(dict4, "type of dict4 is dict?", type(dict4) == io.FileIO)
print(dict4, "type of dict4 is dict?", isinstance(dict4, A))

"""
    descr:Python数据类型转换
        对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
"""
print(int("15810227214") + int(3.1415926))
print(float(" 8.75"))
print(complex(3))
# print(str(A())) #出错啦
print(repr("3+4*5"))  #
print(eval("3+4*5"))  # 表达式字符串计算
print(chr(75))  # 整数转字符
print(ord('A'))  # 字符转整数
print(hex(12))  # 整数转为16进制
print(oct(12))  # 整数转为8进制
print(b)
