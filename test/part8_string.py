#!/usr/bin/env python3
import string

"""
    descr:字符串
"""

"""
    descr:字符串格式化，使用占位符，后期使用元组依次赋值
        %c:格式化字符及其ASCII码
        %s:格式化字符串
        %d:格式化整数
        %u:格式化无符号整数
        %o:格式化无符号八进制数
        %x:格式化无符号十六进制数
        %X:格式化无符号十六进制数大写
        %f:格式化浮点数字,可指定小数点的精度
        %e:科学计数法格式化浮点数
        %g:%f和%e的简写
        %p:用十六进制格式化变量的地址。
        另外：格式化操作符辅助指令如下：
        *:定义宽度或小数点精度
        -:用做左对齐
        +:正数前显示+号
        <sp>:正数前显示空格
        #:8进制前显示'O'，十六进制前显示Ox或OX(取决于#x还是#X)
"""
print("我叫 %s 今年 %d 岁 %c %o-%x-%X" % ("小米", 20, 100, 12, 13, 14))  # 字符串格式化，%c、%s、%d、%f、%e、%g等等
print("身份证号：%+.3f,%#e,%#E,%g" % (1949878239.3242234, 1949878239.3242234, 1949878239.3242234, 1949878239.3242234))
print("%s 是%#xd 岁" % ("姓名", 18))
print("这是%+#x月" % (2))  # 正数显示+号，包括+号在内总共3位的整数(非10进制前面不能不错0和指定长度)
print("这是%0+3d月" % (2))  # 不够前面补0，正数显示+号，包括+号在内总共3位的整数
print("%(name)s 是 %(age)d岁" % {"name": "姓名", "age": 18})  # 参数是字典

"""
    descr:字符串内建函数
"""
str1 = "unsupported format character :\t error"
print(str1.capitalize(), ",", string.capwords(str1))  # 首字母大写
# str.center(width,fillChar)将源字符串str居中放置，前后平均补充字符fillChar直到长度到width
print(str1.center(50, "'"))
print(str1.count("or"))  # str.count(substr[, beg][,end])返回substr在str的beg-end中出现的次数
# str.encode(encoding="utf-8",errors="strict")返回编码字节数组,bytes.decode(encoding="utf-8",errors="strict")返回解码字符串
print((str1 + "中文").encode("gbk").decode("gb2312"))
# str.endswith(substr[, beg][,end])str(在beg和end间的子串)是否以substr结尾，是则返回true，否则false
print(str1.endswith("character"))
print(str1.expandtabs(2))  # str.expandtabs([size=8])将str中指标符tab替换成指定长度(默认是8)的空格后返回
# str.find(sub[,beg][,end])返回sub在str(在beg和end间的子串)中的位置，没有返回-1
print(str1.find("or"))
# print(str1.index("sor"))  # str.index(sub[,beg][,end])返回sub在str(在beg和end间的子串)中的位置，没有报错
print(str1.isalnum(), "dse13.3".isalnum(), "dse133".isalnum(), "中文aa".isalnum())  # str.isalnum()是否str都是字母或数字
print(str1.isalnum(), "dse13.3".isalpha(), "dse133".isalpha(), "sdf d".isalpha(),
      "sdfEd".isalpha())  # str.isalpha()是否str都是字母
print(str1.isdigit(), "321.3".isdigit(), "289 3".isdigit(), "32,234".isdigit(),
      "33".isdigit())  # str.isdigit()是否str都是数字
# str.islower() str中包含大小写的字符中所有都为小写，返回true，否则返回false
print(str1.islower(), "看我中文".islower(), "看我中文A".islower(), "看d我a中e文ad".islower())
# str.isnumeric() str中包含都是数字，不包含其他字符，返回true，否则返回false
print(str1.isnumeric(), "324b".isnumeric(), "324".isnumeric(), "324.524".isnumeric())
# str.isspace() str中包含都是空格，不包含其他字符，返回true，否则返回false
print(str1.isspace(), " ".isspace(), "\t".isspace(), "\r\n".isspace())
# str.istitle() str如果字符串是标题化的(见 title())则返回 True，否则返回 False
print(str1, str1.istitle(), "\r\n", str1.title(), str1.title().istitle(), "\r\n", "我是chinese,right",
      "我是chinese,right".istitle(), "\r\n", "我是chinese,right".title(), "我是chinese,right".title().istitle())
# str.isupper() str中包含至少一个区分大小写的字符,这些字符都是大写，返回true，否则返回false
print(str1.isupper(), "看我中文".isupper(), "看我中文A".isupper(), "看d我a中e文aD".isupper())
# str.join(seq) 以str为串联分隔符将seq中所有元素(元素需要是字符串)拼接成一个字符串后返回
print(" ".join(["it".capitalize(), "all", "is", "me!"]))
# len(str)或str.__len__() 返回str字符串的字符长度
print(str1.__len__(), ",", len(str1))
# str.ljust(width,fillChar)将源字符串str居左放置，后面补充字符fillChar直到长度到width
print(str1.ljust(50, "."))
# str.lower() 将源字符串str中所有大写字母转化为小写字母并返回
print(str1.lower(), ",sdEw中文 weight".lower())
# str.lstrip(char) 截取str字符串左侧的空格或指定字符
print(str1.lstrip(), "   ,sdEw中文 weight".lstrip(), "   ,sdEw中文 weight".lstrip().lstrip(","))
# str1.maketrans(str1,str2) 创建字符映射的转换表
print(str1.maketrans("unc", "UNC"))
# max(str1) 返回字符串中最大的字符
print(max(str1 + "ds中文"))
# min(str1) 返回字符串中最小的字符
print(min(str1 + "ds中文"), ",", min("ds中文"))
# str.replace(str1,str2,max=1) 返回替换str中str1为str2，最多max次
print(str1.replace("un", "Un"), ",", str1.replace("or", "OR", 2))
# str.rfind(sub[,beg][,end]) 返回sub在str(在beg和end间的子串)中的位置,从右开始查，没有返回-1
print("find'or':", str1.find("or"), ",rfind'or':", str1.rfind("or"))
# str.rindex(sub[,beg][,end]) 返回sub在str(在beg和end间的子串)中的位置,从右开始查，没有返回-1
print("index'or':", str1.index("or"), ",rindex'or':", str1.rindex("or"))
# str.rjust(width,fillChar)将源字符串str居右放置，前面补充字符fillChar直到长度到width
print(str1.ljust(50, "-"), ",", str1.rjust(50, "-"))
# str.rstrip(char) 截取str字符串右侧的空格或指定字符
print(str1.center(50, "."), "截取左右字符：", str1.center(50, ".").lstrip(".").rstrip("."))
# str.split(str1,max=str.count(str1)) 返回str按照str1切割后的字符串列表，可设置最多切割次数max
print(str1.split(" "), ";limit 3", str1.split(" ", 3))
# str.splitlines(keepends) 返回str按照换行符分隔成列表，keepends为True则保留换行符，为False则不保留,默认不保留
str2 = "line1\rline2\r\nline3\nline4"
print(str2.splitlines(), ";", str2.splitlines(True))
# str.startswith(str1,beg=0,end=len(str) 判断str是否以str1字符串开头，如果beg,end非空，在str[beg,end]范围内判断
print(str2.startswith("line"), ";", str2.startswith("line", 5), ";", str2.startswith("line", 6))
# str.strip(char) str去掉左右的空格后返回，相当于执行lstrip和rstrip，如果char非空则去掉左右指定字符
str1 = str1.center(50, "-").center(60)
print(str1, ";", str1.strip(), ";", str1.strip().strip('-'))
# str.swapcase(char) str中字母大写变小写，小写变大写
str1 = string.capwords(str1)
print(str1, ";", str1.swapcase())
# str.title() str标题化格式化后返回，所谓标题化格式化指：所有单词首字母大写
print(str1, "<", str1.istitle(), ">", str1.title())
# str.translate(dict) str中字符按照字典替换后返回
str3 = "my family telephone:0713-3247887"
print(str3.translate(str1.maketrans(string.digits, "*" * len(string.digits))))
print(str3.translate(str1.maketrans(string.ascii_lowercase, string.ascii_uppercase)))
print(str3.translate(str1.maketrans(string.ascii_letters, " " * len(string.ascii_letters))).strip())
# str.upper(dict) str中字符小写转化为大写
print(str3.upper())
# str.zfill(width) str字符串右对齐，并在前面填充0到width长度
print(str3.zfill(50))
# str.isdecimal(width) str字符串是否都是十进制字符，是返回True，否则返回False
print(str3.isdecimal(), "32adcde".isdecimal(), "0xaec".isdecimal(), "234".isdecimal())
