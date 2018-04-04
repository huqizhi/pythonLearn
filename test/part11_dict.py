#!/usr/bin/env python3
"""
    descr:字典
    字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。两个重要的点需要记住：
        1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住;
        2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
"""

"""
    descr:字典的初始化、访问、修改、删除
"""
dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict2 = {'abc': 456}
dict3 = {'abc': 123, 98.6: 37}
print("字典dict1:", dict1)
print("字典dict2:", dict2)
print("字典dict3:", dict3)
print("访问字典键值dict1['Alice']:", dict1['Alice'])
# print("访问字典元素dict1['Alice1']:", dict1['Alice1'])  # 没有的key访问会报错
print("修改字典键值dict2['abc']=123456789", end='');
dict2['abc'] = 123456789;
print(";然后dict2['abc']为：", dict2['abc'])
print("dict1['Alice']:", dict1['Alice'], end='');
del dict1['Alice'];
print(";删除键del dict1['Alice']后'Alice' in dict1：", 'Alice' in dict1)
print("清空字典dict1.clear():", dict1.clear(), "；然后dict1为：", dict1)  # 清空字典
print("删除字典del dict1");
del dict1;
print("；然后dict1不存在")  # 删除字典
dict4 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print("重复键的字典dict4={'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}，创建后字典dict4：", dict4)
dict5 = {'a': 1, 1: '年龄', ("x", "y"): (3, 4), '第一位': '小菜鸟', 'c': None, 'Name': "大笨鸟"}
print("字典dict5={'a':1,1:'年龄',('x','y'):(3,4),'第一位':'小菜鸟'}，创建后字典dict5：", dict5)

"""
    descr:字典内置函数&方法
"""
print("字典长度len(dict5):", len(dict5))
print("打印字典str(dict5):", str(dict5))
print("返回类型type(dict5):", type(dict5))
print("浅复制字典dict5.copy():", dict5.copy())
print("创建一个新字典dict.fromkeys(['a', 1, '第一位']):", dict.fromkeys(['a', 1, '第一位']))
print("创建一个新字典dict.fromkeys(['a', 1, '第一位'], 10):", dict.fromkeys(['a', 1, '第一位'], 10))
print("返回键值dict5.get('a', 10):", dict5.get('a', 10), ";返回键值dict5.get('b', 10):", dict5.get('b', 10)
      , ";返回键值dict5.get('c', 10):", dict5.get('c', 10))  # 键不在字典中，返回默认值
print("测试键是否在字典中'a' in dict5:", 'a' in dict5, ";'b' in dict5:", 'b' in dict5)
print("返回字典dict5中所有(key,value)元组组成的列表：", dict5.items())
print("返回字典dict5中所有key组成的列表：", dict5.keys())
print("设置字典dict5的键值默认值并返回值dict5.setdefault('d','就是我啊')：", dict5.setdefault('d', '就是我啊'))
print("设置字典dict5的键值默认值并返回值dict5.setdefault('a','就是我啊')：", dict5.setdefault('a', '就是我啊'))
print("dict5.setdefault('d','就是我啊')在键不存在时添加并设置了默认值，打印字典str(dict5):", dict5)
print("把字典dict5更新到dict4里dict4.update(dict5):", end="");
dict4.update(dict5);
print(dict4)  # 类似jquery的extend方法
print("返回字典dict5中所有value组成的列表：", dict5.values())
print("删除指定键并返回键值dict5.pop('Name'):", dict5.pop('Name'), ";然后dict5为：", dict5)
print("删除指定键不存在并返回默认值dict5.pop('Name', '丢了'):", dict5.pop('Name', '丢了'), ";然后dict5为：", dict5)
print("随机返回并删除字典中的一对键和值dict5.popitem():", dict5.popitem(), ";然后dict5为：", dict5)
