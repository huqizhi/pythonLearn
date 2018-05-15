#! /usr/bin/env python3
"""
    descr:Python3 输入和输出
        Python常见三种输出值的方式:
        1、表达式语句；
        2、print()语句；
        3、第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用；
        另外：如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
            如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
        字符串格式化：
        1、旧式格式化，str1 % str2,str3 操作符也可以实现字符串格式化，右边代入左边,如:
            '常量 PI 的值近似为：%5.3f。' % math.pi；
        2、新式格式化，str1.format(str2,str3) 可以实现格式化，str2、str3默认依次带入str1，如：
            '常量 PI 的值近似为： {}。'.format(math.pi)
            '常量 PI 的值近似为： {0}。'.format(math.pi)
            'Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format({'Google': 1, 'Runoob': 2, 'Taobao': 3})
            print('站点列表 {}, {1}, 和 {other}。'.format('Google', 'Runoob',other='Taobao'))
        3、字符串方法 rjust(leng, char)、ljust(leng, char)、center(leng, char)和zfill(leng)依次表示右对齐左填充char、
            左对齐右填充char、两边平均填充char和左填充0；
        4、'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化，如：
            print('常量 PI 的值近似为： {!r}。'.format(math.pi))
            print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
        5、format格式化占位符在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用，如：
            table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
            for name, number in table.items():
                print('{0:10} ==> {1:10d}'.format(name, number))
        6、直接访问指定参数中的键值{paramIndex[key]}，如：
            table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
            print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
        Python输入：
        1、读取键盘输入input();
        2、读和写文件；
        3.pickle 模块，python的pickle模块实现了基本的数据序列和反序列化。
"""
import math
import pickle

s = 'Hello, Runoob'
print("s = 'Hello, Runoob',show s=", s)
print("str(s)=", str(s))
print("repr(s)=", repr(s))
print("str(1/7)=", str(1 / 7))
# repr能够识别\n等特殊字符
print(r"repr('hello, runoob\n')=", repr('hello, runoob\n'))
x = 10 * 3.25
y = 200 * 200
# repr() 的参数可以是 Python 的任何对象
print("repr((x, y , ('Google', 'Runoob')))=", repr((x, y, ('Google', 'Runoob'))))
# 这里有两种方式输出一个平方与立方的表
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4))
pass
for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x * x, x * x * x))
pass

print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
print('常量 PI 的值近似为 {!r}。'.format(math.pi))
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
pass

## 标准输入，既是键盘输入，读取一整行
str = input("请输入添加到system.properties中test属性的值：")
print("你输入的是：", str)

## 打开文件
file1 = open("C:\\Users\\Administrator\\Desktop\\reportContents.jsp", "rb")
str2 = file1.read(1024)
print("当前位置：", file1.tell())
file1.seek(10, 1)
print("往后移动10个字节，继续读取10个字节：", file1.read(10))
file1.close()
print("读取一行数据：", str2)
file2 = open("C:\\Users\\Administrator\\Desktop\\system.properties", "a+", encoding='utf-8')
file2.write("test={}\n".format(str))
file2.close()

file3 = open(r"C:\Users\Administrator\Desktop\pickle1", "wb")
print("将table={}序列化到{}里".format(table, file3.name))
pickle.dump(table, file3)
data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}
pickle.dump(data1, file3, -1)
print("将data1={}序列化到{}里".format(data1, file3.name))
file3.close()

file4 = open(r"C:\Users\Administrator\Desktop\pickle1", "rb")
print("反序列化{0}:".format(file4.name))
pickleData1 = pickle.load(file4)
print("数据1：{}".format(pickleData1))
pickleData2 = pickle.load(file4)
print("数据2：{}".format(pickleData2))
file4.close()
