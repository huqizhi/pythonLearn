#!/usr/bin/env python3
"""
    descr:Python3 解释器，分为windows和linux（这个是主流）
"""

"""
    descr:设置环境变量
        linux方式为shell命令：PATH=$PATH:{python3path}/bin/python3
        windows方式为cmd命令：set path=%path%;{python3path}
"""

"""
    descr:交互式命令，安装环境变量后即可在命令行输入python进入交互模式
        linux方式为shell命令：python3
        windows方式为cmd命令：python
"""

"""
    descr:脚本式编程，将python命令写入文本文件中，文本文件命名为*.py,然后命令启动
        linux方式：如果文件内部第一行置顶了解释器"#!/usr/bin/env python3",chmod授权后即可直接运行“./filename.py”；
            如果没有也可以通过python命令来运行“python filename.py”（依赖环境变量），或者绝对路径下python目录下执行；
        windows方式为cmd命令："python filename.py"
"""
