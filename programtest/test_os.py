#! /usr/bin/env python3
"""
    descr:os模块，强大的文件或者文件夹操作
"""
import os
import sys

dir1 = r"d:\pythonDir\pythonDir2"
# os.makedirs(dir1)
file1 = open(dir1 + r"\pythontest.txt", "w+")
print(file1.name)
print("fileno:", file1.fileno())
file1.close()
# os.rename(file1.name, file1.name+".bak")
dir2 = r"D:\pythonDir"
cdList = os.listdir(dir2)
for tmpFile in cdList:
    tmpDir = dir2 + "\\" + tmpFile
    isFile = False
    if os.path.isfile(tmpDir):
        isFile = "文件"
    else:
        isFile = "文件夹"
    print(tmpFile, "({}):".format(isFile), os.stat(tmpDir))
pass
print("尝试删除：", dir2)
deleteFlag = False
try:
    print("当做文件删除：", end="")
    os.remove(dir2)
    deleteFlag = True
    print("删除成功")
except:
    print("删除失败", sys.exc_info()[0])
pass
if deleteFlag == False:
    try:
        print("当做文件夹删除：", end="")
        os.rmdir(dir2)
        deleteFlag = True
        print("删除成功")
    except:
        print("删除失败", sys.exc_info()[0])
    pass

if deleteFlag == False:
    try:
        print("当做文件夹递归删除：", end="")
        os.removedirs(dir2)
        deleteFlag = True
        print("删除成功")
    except:
        print("删除失败", sys.exc_info()[0])
    pass
