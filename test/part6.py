#!/usr/bin/env python3
"""
    descr:运算符,有7类，一次为：算术、比较（关系）、赋值、逻辑、位、成员、身份运算符，额外补充还有运算符的优先级
"""

"""
    descr:算术运算符，有7个，依次为+(加)、-(减)、*(乘)、/(除)、%(取模)、**(幂)、//(求余)
"""
print("3 + 5 的值为：", 3 + 5)
print("3 - 5 的值为：", 3 - 5)
print("3 * 5 的值为：", 3 * 5)
print("5 / 3 的值为：", 5 / 3)
print("5 % 3 的值为：", 5 % 3)
print("5 ** 3 的值为：", 5 ** 3)
print("5 // 3 的值为：", 5 // 3)

"""
    descr:比较运算符，有6个，依次为==(等于)、!=(不等于)、>(大于)、>=(大于等于)、<(小于)、<=(小于等于)
"""
print("'中国'=='中国人'", '中国' == '中国人')
print("'中国'!='中国人'", '中国' != '中国人')
print("'中国'>'中国人'", '中国' > '中国人')
print("'中国'>='中国人'", '中国' >= '中国人')
print("'中国'<'中国人'", '中国' < '中国人')
print("'中国'<='中国人'", '中国' <= '中国人')

"""
    descr:赋值运算符，有8个，依次为=(简单赋值)、+=(加法赋值)、-=(减法赋值)、*=(乘法赋值)、
            /=(除法赋值)、%=(取模赋值)、**=(幂赋值)、//=(取整除赋值)
"""
a = 22
b = 10
print("a简单赋值", a, "b简单赋值", b)
a += b
print("a加法赋值a+=b", a)
a -= b
print("a减法赋值a-=b", a)
a *= b
print("a乘法赋值a*=b", a)
a /= b
print("a除法赋值a/=b", a)
a %= b
print("a取模赋值a%=b", a)
a **= b
print("a幂赋值a**=b", a)
a //= b
print("a取整除赋值a//=b", a)

"""
    descr:位运算符，依次为&(按位与)、|(按位或)、^(按位异或)、~(按位取反)、<<(做移动)、>>(右移动)
"""
a = 60  # 二进制为0011 0000
b = 13  # 二进制为0000 1101
print("a=60,二进制为0011 0000")
print("b=13,二进制为0000 1101")
print("a&b为", a & b)
print("a|b为", a | b)
print("a^b为", a ^ b)
print("~a为", ~a)
print("b<<2为", b << 2)
print("a>>2为", a >> 2)

"""
    descr:逻辑运算符，依次为and(布尔与)、or(布尔或)、not(布尔非)
"""
a = 10
b = 20
if a and b:
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if a and b:
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")
if not a and b:
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

"""
    descr:成员运算符，依次为in(包含)、not in(不包含)
"""
a = 10
b = 20
c = [1, 3, 4, 10, 30]
print("a=", a)
print("b=", b)
print("c=", c)
if a in c:
    print("a包含在c中")
else:
    print("a不在c中")

if b not in c:
    print("b不包含在c中")
else:
    print("b在c中")

"""
    descr:身份运算符,依次为is(是)、is not(不是)，是判断两个标识符是不是引用自一个对象
"""
a = "我们都有一个家，名字叫中国"
b = "我们都有一个家，名字叫中国"
print("a是’", a, "'")
print("b是’", b, "'")
if a is b:
    print("a is b")
else:
    print(" a is not b")

b = "姐妹多"
print("修改后，b是’", b, "'")
if a is not b:
    print("a is not b")
else:
    print(" a is b")
