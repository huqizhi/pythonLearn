#!/usr/bin/env python3

"""
    descr:循环语句，包括while、for及其子句continue、break,另外有range辅助函数
"""

"""
    descr:while循环
"""
num = 100
sum = 0
counter = 1
while counter <= num:
    sum += counter
    counter += 1

print("1 到 %d 间的数据和为：%d " % (num, sum))

"""
    descr:while...else...循环,当循环完所有数据时执行else(既是非break状态执行while结束后会执行else)
"""
count = 0
while count < 5:
    print(count, " 小于5")
    count += 1
else:
    print("%d 大于等于5" % count)

"""
    descr:for循环,可以遍历任何序列的项目，如一个列表或者一个字符串。
"""
languages = ["C", "C++", "Perl", "Python"]
for lan in languages:
    print(lan)

"""
    descr:for...else...循环,当循环完所有数据时执行else(既是非break状态执行for结束后会执行else)
"""
for lan in languages:
    if lan == 'Perl':
        print("找到了目标")
        break
    print("列表数据：", lan)
else:
    print("列表没有数据")

languages = []
for lan in languages:
    if lan == 'Perl':
        print("找到了目标")
        break
    print("列表数据：", lan)
else:
    print("列表没有数据")

print("执行完成!")

"""
    descr:range()函数,辅助查询列表
"""
for i in range(10):
    print("rang(10)生成数:", i)

for i in range(20, 30):
    print("range(20, 30)生成数:", i)

for i in range(20, 30, 3):
    print("range(20, 30, 3)生成数:", i)

"""
    descr:for和range函数合作，以下标方式遍历列表
"""
languages = ["世界那么美!", "我想去看看！", "13"]
for i in range(len(languages)):
    print("languages中第 %d 个元素数为：%s" % (i + 1, languages[i]))
else:
    print("languages 没有数据")

"""
    descr:break(终止循环)和continue(跳过当次循环)语句及循环中的else(非break时循环完成才会执行)子句
"""
zhishulist = []
for n in range(2, 10):
    for x in zhishulist:
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
        zhishulist.append(n)

"""
    descr:pass 语句,空语句，是为了保持程序结构的完整性。
"""
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
