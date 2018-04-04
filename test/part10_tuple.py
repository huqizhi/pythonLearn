#!/usr/bin/env python3
"""
    descr:元组，元组与列表类似，区别在于元素元素不可修改，如果元素
"""

"""
    descr:元组的初始化
"""
tup1 = ('Google', 'Runoob', 1997, 2000)  # 标准创建方式(ele1, ele2 , ...)
tup2 = (1, 2, 3, 4, 5)  # 标准创建方式(ele1, ele2 , ...)
tup3 = 'this ', ' is ', ' egg ', 2008;  # 不加小括号，用逗号和分号来初始化
tup4 = ()  # 创建空元组
tup5 = (1)  # 此时tup4是数字类型，并不是元组
tup6 = (1,)  # 创建单元素元组需要这样(ele1,)，否则会把小括号当做运算符或者其他什么的
print("输出元组tup1：", tup1, ";tup2：", tup2, ";tup3：", tup3, ";tup4：", tup4, ";tup5：", tup5, ";tup6：", tup6)

"""
    descr:访问元组或元组元素、修改元组(元组连接)、删除元组(不能删除元组元素)
"""
print("访问元组tup1的第一个元素tup1[0]：", tup1[0], ";访问元组的第一个到第三个元素tup1[0:3]:", tup1[0:3])
print("给将tup1和tup2连接来改变tup1=tup1+tup2", end="");
tup1 = tup1 + tup2;
print("，然后tup1为：", tup1)
print("tup6为：", tup6);
del tup6;  # print(";删除后，tup6为：", tup6)  # 删除后不可访问，否则会报错

"""
    descr:元组运算符
"""
print("计算tup1的元素个数len(tup1):", len(tup1))
print("连接元组tup2和tup3为tup2+tup3=:", tup2 + tup3)
print("复制元组('.',)*3：", ('.',) * 3)
print("元素是否存在2008 in tup3:", 2008 in tup3, ";元素是否存在2018 in tup3:", 2018 in tup3)
print("依次访问元组tup1的元素 for a in tup1: print(a,) ,输出如下：")
for a in tup1:
    print(a, end=',')
print()

"""
    descr:元组元素索引和截取
"""
print("访问tup1第五个元素tup1[4]:", tup1[4])
print("访问tup1倒数第二个元素tup1[-2]:", tup1[-2])
print("截取元素，从第二个开始后的所有元素：", tup1[1:])
print("截取元素，从第二个到第五个的所有元素：", tup1[1:5])

"""
    descr:元组内置函数
"""
print("计算元组元素个数len(tup3)：", len(tup3))
print("返回元组中最大值max(tup2)：", max(tup2))
print("返回元组中最小值min(tup2)：", min(tup2))
print("将列表转换为元组tuple([3,2,8,7,4])：", tuple([3, 2, 8, 7, 4]))
