#! /usr/bin/env python3
"""
    descr: 文件的读写
        0、open(filename, mode, [encoding='SysEncoding']),mode取值r、r+、rb、rb+、w、w+、wb、wb+、a、a+、ab、ab+;
        1、f.read([size]) 读取指定大小的文件内容,当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
        2、f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
        3、f.readlines([size]) 将返回该文件中包含的所有行。size非空, 则读取指定长度的字节, 并且将这些字节按行分割。
        4、f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
        5、f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
        6、f.seek(offset, [from_what]) 改变文件当前的位置,from_what 的值, 如果是 0、1、2依次表示开头、当前位置、结尾，例如：
          seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
          seek(x,1) ： 表示从当前位置往后移动x个字符
          seek(-x,2)：表示从文件的结尾往前移动x个字符
          from_what 值为默认为0，即文件开头。
          注意：在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位，意即from_what只能为0，其他报错。
        7、f.close() 关闭文件并释放系统的资源
        8、file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
        9、file.fileno() 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
        10、file.isatty() 如果文件连接到一个终端设备返回 True，否则返回 False。
        11、file.next() 返回文件下一行。
        12、file.truncate([size]) 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；
            截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小
        13、file.writelines(sequence) 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
"""
file1 = open(r"C:\Users\Administrator\Desktop\system.properties", "w+", encoding="utf-8")
print("文件是否有第三方在打开使用中：", file1.isatty())
print("文件描述符：", file1.fileno())
file1.close()
