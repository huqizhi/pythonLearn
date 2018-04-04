#!/usr/bin/env python3
"""
    descr:列表
"""
list1 = ['Google', 'Runoob', 1997, 2000]
print("list1列表原型：", list1)
print("第三个元素为 : ", list1[2])
list1[2] = 2001
print("更新后的第三个元素为 : ", list1[2])
del list1[2]
print("list1列表del list1[2]后： : ", list1)

"""
    descr:列表脚本操作符
"""
print("list1长度len(list1):", len(list1))
list1 = ["1", "李雷", "你好"]
list2 = ["2", "韩梅梅", "你也好"]
print("list1:", list1, ";list2:", list2, ";合并后为：", list1 + list2)
print("列表:", ["X", "Y"], "*4重复四遍:", ["X", "Y"] * 4)
print("判断X是否在列表中'X' in ", ["X", "Y"], "中:", "X" in ["X", "Y"])
print("迭代列表for a in ", list1, ": print(x, end=','):", end="")
for a in list1:
    print(a, end=",")
print()

"""
    descr:列表截取与拼接
"""
print("读取", list1, "[1]第二个元素：", list1[1])
print("读取", list1, "[-2]倒数第二个元素：", list1[-2])
print("读取", list1, "[1:]第二个元素开始的所有元素：", list1[1:])

"""
    descr:嵌套列表
"""
print("列表嵌套[list1,list2]:", [list1, list2])

"""
    descr:列表函数&方法
"""
print("list1为：", list1, ",如下操作值为：")
print("\tlen(list1):", len(list1))
print("\tmax(list1):", max(list1))
print("\tmin(list1):", min(list1))
tuple1 = ("what's ", "the ", "fuck?")
print("\t元组tuple1=", tuple1, "转化为列表list[tuple1]:", list(tuple1))

"""
    descr:包含方法
"""
print("list1为：", list1, ",如下操作值为：")
print("末尾添加新对象list2和'你好'后变为:", end="");
list1.append(list2);
list1.append("你好");
print(list1)
print("统计元素'你好'出现次数:", list1.count("你好"))
print("末尾添加另一个列表多个值，拓展后为:", );
list1.extend(list2);
print(list1)
print("第一个'你好'的位置：", list1.index("你好", 3))
print("插入元素list1.insert(1,'100'):", end="");
list1.insert(1, "100");
print(list1)
print("移除最后元素list1.pop():", list1.pop(), ";然后列表为：", list1)
print("移除最后元素list1.pop(-2):", list1.pop(-2), ";然后列表为：", list1)
print("删除第一个“你好”元素list1.remove(“你好”):", list1.remove("你好"), ";然后列表为：", list1)
print("反转列表list1.reverse():", list1.reverse(), ";然后列表为：", list1)
print("删除列表中数组元素：", list1.pop(2), ";列表排序list1.sort([func]):", list1.sort(), ";然后列表为：", list1)
listK = list1.copy();
listK.append("新的");
print("复制列表list1.copy()：", listK, ";原列表：", list1)
print("清空列表list1.clear()：", list1.clear(), "后列表为：", list1)
