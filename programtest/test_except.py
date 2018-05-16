#! /usr/bin/env python3
"""
    descr:错误和except异常。
        1.语法错误 ,Python 的语法错误或者称之为解析错，这里叫错误；
        2.即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常；
        3.异常语句：
            try:
                ...
            except ExceptObject1:
                ...
            except ExceptObject2:
                ...
            except (ExceptObject3, ExceptObject4):
                ...
            except:
                ...
            else:
                ...
            3.1、try语句按照如下方式工作:
                首先，执行try子句（在关键字try和关键字except之间的语句）;
                如果没有异常发生，忽略except子句，try子句执行后结束;
                如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的
                    名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码;
                如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
            3.2、一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
            3.3、处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
            3.4、一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组。
            3.5、最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以打印错误信息并再次把异常抛出。
            3.6、可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后，它在try子句没有发生任何异常的时候执行。
        4、抛出异常：raise 语句抛出一个指定的异常
            4.1、raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
            4.2、如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
        5、定义清理行为：finally子句，它定义了无论在任何情况下都会执行的清理行为。
            5.1、不管 try 子句里面有没有发生异常，finally 子句都会执行。
            5.2、如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，
                那么这个异常会在 finally 子句执行后再次被抛出。
        6、预定义的清理行为：一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
            关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法。
        7、用户自定义异常
            你可以通过创建一个新的exception类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承。

"""
import sys

## 语法错误 ,Python 的语法错误或者称之为解析错，是初学者经常碰到的
# while True print('Hello world')

## 异常, 异常以不同的类型出现，这些类型都作为信息的一部分打印出来: 例子中的类型有 ZeroDivisionError，NameError
##  和 TypeError。错误信息的前面部分显示了异常发生的上下文，并以调用栈的形式显示具体信息。
# ZeroDivisionError: division by zero
# a = 10 * ( 1 / 0 )
# NameError: name 'a' is not defined
# b = 4 + a * 3
# TypeError: must be str, not int
# c =  '2' + 2
## 异常处理
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again   ")
pass


def isVarExists(varName, list1):
    # 第一种方法使用内置函数dir()：
    return varName in list1


try:
    f = open(r'C:\Users\Administrator\Desktop\system.properties1')
    s = f.readline()
    i = int(s.strip())
    k = i / 10
    # k = i/10
except (RuntimeError, TypeError, NameError) as err:
    print("error: {0}".format(err))
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print("没有任何异常")
finally:
    if isVarExists('f', dir()):
        print("关闭打开的文件")
        f.close()
    else:
        print("没有资源需要关闭")
        pass
pass
print("文件是否关闭了：", not isVarExists('f', dir()))
# 打开的文件并没有关闭
f = open(r"C:\Users\Administrator\Desktop\system.properties")
for line in f:
    print(line, end="")
print("文件是否关闭了：", not isVarExists('f', dir()))
# with语句保证了文件正常关闭f
with open(r"C:\Users\Administrator\Desktop\system.properties") as tmpFile:
    for line in tmpFile:
        print(line, end="")
print("文件是否关闭了：", not isVarExists('tmpFile', dir()))


class MyError(Exception):
    # 构造函数
    def __init__(self, value):
        self.value = value

    # 对象输出函数
    def __str__(self):
        return repr(self.value)


try:
    raise MyError(234 * 14)
except Exception as e:
    print("error class:", type(e))
    print("error:", e)
    print("error:", e.value)
