#!/usr/bin/env python3
import random

"""
    descr:条件控制
"""
var1 = 100
if var1:
    print("1- if表达式条件为true:", var1)

var2 = 0
if var2:
    print("2- if表达式条件为true", var2)

print("Good bye!")

# if ... elif ... else...

age = int(input("请输入你家狗狗的年龄："))
print()
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于14岁的人。")
elif age == 2:
    print("相当于22岁的人。")
else:
    human = 22 + (age - 2) * 5
    print("相当于人类年龄:", human)

# 退出提示
# input("请输入enter键退出")
print("\n==========开始数字猜谜游戏===========")
number = random.choice(range(100))
guess = -1
while guess != number:
    guess = int(input("请输入你猜的数字(1-100)之间:"))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    else:
        print("猜的数字大了...")

print("==========数字猜谜游戏结束===========")
print("==========测试数字是否被2、3整除===========")
num = int(input("输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")
