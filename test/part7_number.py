#!/usr/bin/env python3
import math
import random

"""
    descr:数字（number),依次有int,float,complex
"""
print(10, int(8), 10.0, float(12), 10 + 10j, complex(10, 20))

"""
    descr:数学函数
"""
print(abs(-100))  # 绝对值
print(math.fabs(-100))  # 浮点数绝对值
print(math.ceil(100.3))  # 向上取整
print((10 > 100) - (10 < 100))  # 比较函数 math.cmp(100.3),3.0里使用(x>y)-(x<y)来替换
print(math.exp(1))  # e的n次幂
print(math.floor(100.3))  # 向下取整
print(math.log(math.e), math.log(10, 100))  # 返回对数，math.log(x,xbase),xbase可选默认为math.e
print(math.log2(8), math.log10(100))  # 返回以2为基的对数，返回以10为基的对数
print(max("132423932"), max([1, 3, 5, 324, 8, 22]), max(1, 3, 7, 14, 6, 4), max("adfeiiw"))  # 返回最大数
print(min("32423932"), min([5, 324, 8, 22]), min(14, 6, 4), min("adfeiiw"))  # 返回最小数
print(math.modf(10.324))  # math.modf(x)返回小数部分和整数部分，数值符号同参数，整数部分已浮点型表示
print(pow(10, 5))  # pow(x,y)返回x的y次幂
print(round(10.23428732, 2), round(10.23428732, 4))  # round(x,y)返回x的四舍五入数，保留y位小数
print(math.sqrt(16))  # math.sqrt(x)返回x的平方根

"""
    descr:随机数函数
"""
print(random.choice("dsewir18234099"), random.choice([32, 837, 16, 39, 68, 7]),
      random.choice(range(100)))  # random.choice(list)返回随机元素
print(random.randrange(10, 30, 3))  # random.randrange(a, b, c)返回a-b直接递增为c的数组成的列表中任一个数
print(random.random())  # random.random()返回0-1之间的随机实数
# random.seed([1, 3, 5, 7, 9])  # 改变随机数的种子seed
print(random.random())  #
list = ["s", "i", "k", "s"]
random.shuffle(list)
print(list)  # random.shuffle(list)对数组随机排序
print(random.uniform(0.5, 2.0))  # random.uniform(x, y) 返回x、y之间一个随机实数

"""
    descr:三角函数
"""
print(round(math.sin(math.pi / 3), 2))  # math.sin(x)返回x弧度的正弦值
print(round(math.cos(math.pi / 3), 2))  # math.cos(x)返回x弧度的余弦值
print(round(math.tan(math.pi / 3), 2))  # math.tan(x)返回x弧度的正切值
print(round(math.degrees(math.pi / 3), 2))  # math.degrees(x)返回弧度对应的角度
print(round(math.radians(60), 2))  # math.radians(x)返回角度对应弧度
print(round(math.asin(0.5), 2))  # math.asin(x)返回x的反正弦弧度值
print(round(math.acos(0.87), 2))  # math.acos(x)返回x的反正弦弧度值
print(round(math.tan(math.pi / 4), 2))
print(round(math.atan(math.pi / 4), 2))  # math.atan(x)返回x弧度的反正弦弧度值
print(math.hypot(3, 4))  # math.hypot(x, y)返回欧几里德范数sqrt(x*x+y*y)
print(math.atan2(1, 1))  # math.atan2(y, x)返回X及Y坐标的反正切值

"""
    descr:数学常量
"""
print(math.pi)  # 圆周率 π
print(math.e)  # 数学常量e, e及自然常数
