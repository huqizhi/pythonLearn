#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import keyword

"""
    descr:关键字查看
"""
print("输出python内置的关键字：",keyword.kwlist)

"""
    descr:单行注释，多用于说明关键语句说明或者复杂步骤分隔
"""
# 第一个注释
print("Hello,Python!")# 第二个注释
# 第一行注释
# 第二行注释
# 第三行注释

"""
    descr:多行注释，多用于说明类或者方法的使用
"""
'''
第一行注释
第二行注释
第三行注释
'''
"""
第四行注释
第五行注释
第六行注释
"""

"""
    descr:缩进表示代码块，要求块内缩进一致性
"""
if True:
    print("True")
    print(2**5)
else:
    print("False")
# print("yes")# 缩进不一致，会导致运行错误
    print("yes")

"""
    descr:语句用反斜杠(\)来实现，有语句块开始结束符的不需要，如[]、{}、()等
"""
total = 1**2+\
        2**3+\
        3**4+\
        4**5
print(total)
total = ["abc",
         "def",
         "ghi"]
print(total)

'''
    descr:数据类型--数字类型
'''
print("int (整数)：", 1)
print("bool (布尔)：", True)
print("float (浮点数)：", 1.23, ",", 3E-2)
print("complex (复数)：", 1+3j, ",", complex(2, 4))

'''
    descr:数据类型--字符串
'''
print('第一个字符串，', "第二个字符串，", '''
多行字符串开始：
多行第一行，
多行第二行；
''', """
多行第三行，
多行第四行；
""")




