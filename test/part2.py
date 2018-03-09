#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""
    descr:基础语法
"""
import keyword
import sys

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
print('第一个字符串，', "第二个字符串，\n", r"第三个\n字符串，", '''
多行字符串开始：
多行第一行，
多行第二行；
''', """
多行第三行，
多行第四行；
""")
print("this" "is" "a" "book", ",", "my " + "book", "!" * 2)
str = "abcdefg"
print(str)
print(str[0])
print(str[3])
print(str[0:-1])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "你好")
print("你\n好")
print(r"你\n好")

"""
    descr:空白行分隔开类、方法和方法的开始，这是一个好习惯
"""

"""
    descr:等待用户输入后继续
"""
inputStr = input("\n\n按下 enter 键后退出。")

"""
    descr:一行执行多条语句，用逗号“,”分隔
"""
x = "runoob";
sys.stdout.write(x + "\n")

"""
    descr:多个语句构成代码组(缩进相同的一组语句构成一个代码块，我们称之代码组)
"""
if inputStr == "runoo":
    print("输入了：runoo")
elif inputStr == "runoob":
    print("输入了：runoob")
else:
    print("输入了：", inputStr)

"""
    descr:print输出默认是换行的，要想不换号，语句里末尾加上 end=""
"""
x = 1
y = 2
# 换行输出
print(x)
print(y)
# 不换行输出
print(x, end='')
print(y, end='')
print()

"""
    descr:import 与 from...import -- 示例参考part2-import.py和part2-from-import.py
        在 python 用 import 或者 from...import 来导入相应的模块。
        将整个模块(somemodule)导入，格式为： import somemodule ;
        从某个模块中导入某个函数,格式为： from somemodule import somefunction;
        从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc;
        将某个模块中的全部函数导入，格式为： from somemodule import *;
        区别：import内函数调用需要写成somemodule.firstfunc;而from ... import 后则可以直接写firstfunc;
        
"""

"""
    descr:命令行参数,很多程序可以执行一些操作来查看一些基本信息，Python可以使用-h参数查看各参数帮助信息;
        程序中也可以通过help(funname)函数来查看函数的参数列表和规范的文档，“:q”即可退出;
        如果仅仅想得到文档字符串，可以print(funname.__doc__)；
"""
# 如下实例，查看 max 内置函数的参数列表和规范的文档
print(max)
print(max.__doc__)
print(max([1, 3, 2, 8, 7, 10, 5]))
print(max(1, 3, 2, 8, 7, 10, 5))
