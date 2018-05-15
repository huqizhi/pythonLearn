#!/usr/bin/env python3
import random

"""
    descr:函数，涉及关键字、格式、参数、返回值、参数域

"""


# 计算面积
def area(width, height):
    return width * height


pass
w, h = 4, 5
print("width=%d,height=%d,area=%d" % (w, h, area(w, h)))

"""
   descr:参数传递
        1.参数分为可变类型（列表和字典）和不可变类型(字符串、元组、数字)；--python类型属于对象，变量仅是引用
        2.参数传递时，可变类型是引用传递，不可变类型是复制对象传递；
        3.参数类型：必须参数、关键字参数(调用时按参数名传参，可不用在意顺序)、默认参数(参数有默认值)、不定长参数(参数个数不固定)
"""


def sum(list1, size):
    count = 0
    for x in list1:
        count += x
    # 引用传递队列（一个对象），内部改变后，函数体外也会变化
    list1.append(count)
    # 复制传递数字(内外是两个不同的对象了），内部改变后（一个对象的变化自然不会导致另一个对象变化)，外部并不会改变
    size = len(list1)
    return count


listTmp = list(range(2, 200, random.randrange(5, 10)))
size1 = len(listTmp)
print(listTmp, "暂计数:", size1)
print("求和结果为:", sum(listTmp, size1))
print("求和后为：", listTmp, "错误计数:", size1, "真正数量:", len(listTmp))


# 必须参数：申明的2个参数，调用时需要2个参数
def fnMustParam(a, b):
    print("a=", a, ";b=", b)
    return a * b


print("必须参数：fnMustParam(10, 11)=", fnMustParam(10, 11))
print("关键字参数：fnMustParam(b=15, a=12)", fnMustParam(b=15, a=12))


def fnDefaultParam(name, age=10):
    return "name:%s;age:%d" % (name, age)


print("不使用默认值：fnDefaultParam('大龙', 11)=", fnDefaultParam('大龙', 11))
print("使用默认值：fnDefaultParam('涛哥')", fnDefaultParam('涛哥'))


def fnDynLenParam(*listEle):
    return list(listEle)


print("2参数构成的列表：fnDynLenParam('新浪', '浪潮'):", fnDynLenParam('新浪', '浪潮'))
print("4参数构成的列表：fnDynLenParam('新浪', '浪潮', '中信', '中兴'):", fnDynLenParam('新浪', '浪潮', '中信', '中兴'))

"""
    descr:匿名函数lambda
        1.lambda 只是一个表达式，函数体比 def 简单很多;
        2.lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去;
        3.lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
"""


def jiecheng(x):
    chengji = lambda x: x ** x
    result = 0
    while x > 1:
        result += chengji(x)
        x -= 1
    return result


print("匿名函数求阶乘：", jiecheng(5))

"""
    descr:return语句
         1.语句用于退出函数;
         2.选择性地向调用方返回一个表达式,不带参数值的return语句返回None;
         3.函数中没有return语句也默认返回值为None。
"""


# 返回多个参数中的最大值
def fnReturnValue1(*intp):
    return max(intp)


def fnReturnNone(*intp):
    print(intp, "中最大值是:", max(intp))


print("fnReturnValue1(10,9,8,20,38):", fnReturnValue1(10, 9, 8, 20, 38))
print("fnReturnNone(10,9,8,20,38):", fnReturnNone(10, 9, 8, 20, 38))

"""
    descr:变量作用域
        1.包括四类：
            L （Local） 局部作用域
            E （Enclosing） 闭包函数外的函数中
            G （Global） 全局作用域
            B （Built-in） 内建作用域
            以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），
                再找不到就会去全局找，再者去内建中找。
        2.Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
            其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
            也就是说这些语句内定义的变量，外部也可以访问。
"""
# 4作用域
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


# if/elif/else/、try/except、for/while等由于不会引入新作用域，语句外可以访问。

if True:
    msg = "I am in if sentence."
    print("if sentence inner:", msg)
print("if sentence outer:", msg)

"""
    descr:全局变量和局部变量
        1.定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域;
        2.局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问;
        3.调用函数时，所有在函数内声明的变量名称都将被加入到作用域中；
        4.当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
"""
# 全局变量和局部变量
total = 0;  # 这是一个全局变量


def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total;


sum(10, 20);
print("函数外是全局变量 : ", total)

#  修改全局变量，就要用到global
num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()
print(num)


#  修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()
print(num)
