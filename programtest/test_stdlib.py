#! /usr/bin/env python3
"""
    descr: 标准库概览
        1、操作系统接口，os模块和shutil模块；
        2、文件通配符，glob模块；
        3、命令行参数, sys模块；
        4、字符串正则匹配, re模块；
        5、数学，math模块和random模块；
        6、访问互联网，最简单的两个是urllib.request模块和smtplib模块；
        7、日期和时间，datetime模块；
        8、数据压缩，zlib模块；
        9、性能度量，timeit模块；
        10、模块测试，doctest模块和unittest模块。
"""
import glob
import math
import os
import random
import re
import shutil
import sys
import urllib.request
import zlib
from datetime import date
from timeit import Timer

if __name__ == "__main__":
    ## 1、操作系统接口
    print("当前的工作目录:", os.getcwd())  # 返回当前的工作目录
    print("修改当前的工作目录:", os.chdir(r'D:\tmp2'), ";新工作目录：" + os.getcwd())  # 修改当前的工作目录
    print("执行系统命令 mkdir:", os.system('mkdir today'))  # 执行系统命令 mkdir
    # 建议使用 "import os" 风格而非 "from os import *"。这样可以保证随操作系统不同而有所变化的 os.open()
    # 不会覆盖内置函数 open()。在使用 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:
    print("dir(os):", dir(os))
    # print("help(os):", help(os))
    # 针对日常的文件和目录管理任务，:mod: shutil 模块提供了一个易于使用的高级接口:
    os.chdir(r'today')  # 进入today目录
    shutil.copyfile(r'pickle1', r'pickle2')  # 复制文件
    # shutil.move(r'reportContents.jsp', r'reportContents.jspx') # 修改文件名

    ## 2、文件通配符，glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
    print("glob.glob('*.properties'):", glob.glob('*.properties'))

    ## 3、命令行参数，通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
    print("sys.argv:", sys.argv)
    # 错误输出重定向和程序终止,sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，
    # 后者也可以用于显示警告和错误信息。大多脚本的定向终止都使用 "sys.exit()"。
    print(r"sys.stderr.write('Warning, log file not found starting a new one\n'):")
    sys.stderr.write('Warning, log file not found starting a new one\n')

    ## 4、字符串正则匹配，re模块为高级字符串处理提供了正则表达式工具，对于复杂的匹配和处理提供了简洁、优化的解决方案。
    print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))  # 查找f开头的单词
    print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat the in the the hat'))  # 查找任意单词，只能出现一次
    # 如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试
    print(" 'tea for too'.replace('too', 'two'):", 'tea for too'.replace('too', 'two'))

    ## 5、数学,math模块为浮点运算提供了对底层C函数库的访问,而random提供了生成随机数的工具。
    print("math.cos(math.pi / 4):", math.cos(math.pi / 4))  # cos(π/4)
    print("math.log(1024, 2):", math.log(1024, 2))  # 求1024以2为底的指数
    # 随机取列表元素
    print("random.choice(['apple', 'pear', 'banana']):", random.choice(['apple', 'pear', 'banana']))
    print("random.sample(range(100), 10):", random.sample(range(100), 10))  # 随机从列表中取出10个样本
    print("random.random():", random.random())  # 随机浮点数 0-1之间
    print("random.randrange(6):", random.randrange(6))  # 随机获取一个小于等于6的整数

    ## 6、有几个模块用于访问互联网以及处理网络通信协议，用于处理从 urls 接收的数据的 urllib.request
    for line in urllib.request.urlopen('http://www.baidu.com'):
        line = line.decode("utf-8")  # 编译二进制数据为文本
        print(line)
    pass

    # 用于发送电子邮件的 smtplib
    '''
    server = smtplib.SMTP('smtp.exmail.qq.com')
    server.set_debuglevel(1)
    server.login("qizhi@chaoxing.com", "123xx45")
    server.sendmail('qizhi@chaoxing.com', '951882534@qq.com',
                  """
                    To: 951882534@qq.com
                    From: qizhi@chaoxing.com
                    
                    Beware the Ides of March.    
                """)
    server.quit()
    '''
    ## 7、日期和时间，datetime模块为日期和时间处理同时提供了简单和复杂的方法，实现的重点放在更有效的处理和格式化输出。
    now = date.today()
    print("now:", now)
    print("date:", date(2003, 12, 2))
    print(r'now.strftime("%m-%d-%y. %d %b %Y is a %A."):', now.strftime("%m-%d-%y. %d %b %Y is a %A."))
    # 支持日历计算
    birthday = date(1964, 7, 31)
    print("birthday:", birthday, ";days:", (now - birthday).days)

    ## 8、数据压缩，zlib模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
    s = b'witch which has which witches wrist watch'
    print("s:", s, ";len(s):", len(s))
    t = zlib.compress(s)
    print("t = zlib.compress(s):", t, ";len(t):", len(t))
    print("zlib.decompress(t):", zlib.decompress(t))
    print("zlib.crc32(s):", zlib.crc32(s))

    ## 9、性能度量，timeit模块度量不同方法之间的性能差异
    print(r'Timer("t=a;a=b;b=t", "a=1;b=2").timeit()拆分交换耗时: ', Timer("t=a;a=b;b=t", "a=1;b=2").timeit())
    print(r'Timer("a,b = b,a", "a=1;b=2").timeit()元组封装耗时: ', Timer("a,b = b,a", "a=1;b=2").timeit())

    ## 10、模块测试，doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
    # 通过用户提供的例子，它强化了文档，允许doctest模块确认代码的结果是否与文档一致
