#! /usr/bin/env python3
"""
    descr:模块，模块说明：
        1、每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用；
        2、一个模块被另一个程序第一次引入时，其主程序将运行。若需要区分模块测试和外部调用可用__name__属性；
            __name__ == "__main__"表示模块本身作为主程序运行，否则为外部调用（全包名模块限定名）；
        3、dir(modulename) 函数，可以罗列模块所有定义名称(如果modulename为空为当前模块)，以字符串列表形式方位；
        4、标准模块，Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到；
        5、包,包是一种管理 Python 模块命名空间的形式，采用"点模块名称",形如p1.p2.moduleK;
        6、from package import * 导入全包，如果包定义文件 __init__.py 存在，则以__all__ 的列表变量为准，此变量
            没有或者为空则不导入任务子模块，当然__init__.py初始化代码依然会运行；
        想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
        import module1[, module2[,... moduleN]
        1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
        2、sys.argv 是一个包含命令行参数的列表。
        3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。

        导入一个指定的部分到当前命名空间中，语法如下：
        from…import 语句
        1、能够简化调用，当然也可以重新函数应用来简化，如：fnK = package1.package2...fn;
        2、。
"""
import math
import sys
from math import sqrt

import programtest.test_iterANDnext

if __name__ == "__main__":
    print('命令行参数如下:')
    for i in sys.argv:
        print(i)

    print('\n\nPython 路径为：', sys.path, '\n')
    iter1 = programtest.test_iterANDnext.fibonacci(20)
    print("迭代器iter1:")
    while (True):
        try:
            print(next(iter1), end=",")
        except StopIteration:
            print()
            break
    print()

    print("\"import math\",math.pow(2, 10)=", math.pow(2, 10))
    print("\"import math\",math.sqrt(25)=", math.sqrt(25))
    print("\"from math import sqrt\",sqrt(25)=", sqrt(25))
    print("\"dir(sys):\"", dir(sys))
    print("\"dir():\"", dir())
    del i
    print("\"dir():\"", dir())
    del iter1
    print("\"dir():\"", dir())
    print("sys.base_exec_prefix:", sys.base_exec_prefix)
    pass;
