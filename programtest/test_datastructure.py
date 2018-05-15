#!/usr/bin/env python3
from collections import deque

"""
    descr:Python3 数据结构,
"""
"""
    descr:列表，线性数据结构--FIFO队列和LIFO堆栈
    --Python中列表是可变的，这是它区别于字符串和元组的最重要的特点：列表可以修改，而字符串和元组不能。
"""
list1 = [1, "a", "2", 4, "b", 3]
print("list1=", list1)
# list.append(x) 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x] 或 a[len(a)]=x。
print("list1.append('d'):", list1.append('d'), end=';list1=');
list1[len(list1):] = [4];
print(list1)
# list.extend(L) 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L
list2 = ["大中国", "红塔山", "新东方", "超星", "微信", "阿里巴巴"]
print("list2=", list2)
print("list1.extend(list2):", list1.extend(list2), list1)
# list.insert(i, x) 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，
#   例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(ind, x)当ind>=len(a)时相当于 a.append(x) 。
print("list2.insert(0,'e'),list2.insert(8,'end'),list2=", end="");
list2.insert(0, 'e');
list2.insert(10, 'end');
print(list2)
# list.remove(x) 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误--可以先用in判断。
print("list2.remove('微信'),list2=", end="");
list2.remove('微信');
print(list2)
print("'ddsdf' in list2:", 'ddsdf' in list2)
# list.pop([i]) 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。
print("list2.pop():", list2.pop(), ";list2.pop(2):", list2.pop(2), ";list2=", list2)
# list.clear() 移除列表中的所有项，等于del a[:]。
print("list2=", list2, ";list2.clear(),list2=", end="");
list2.clear();
print(list2)
# list.index(x) 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
print("list1=", list1, ";list1.index('a'):", list1.index('a'), ";'as' in list1", "as" in list1)
# list.count(x)	返回 x 在列表中出现的次数。
print("list1=", list1, ";list1.count(4):", list1.count(4), ";list1.count('as'):", list1.count("as"))
# list.sort()	对列表中的元素进行排序--需要列表所有元素为同一种类型，否则会报错。
# print("list1=", list1, ";\r\tlist1.sort():");list1.sort(); print(list1); #会报错
list3 = ["从", "列", "表", "的", "指", "定", "位", "置", "移", "除", "元", "素"];
print("list3=", list3);
list3.sort();
print("\tlist3.sort():", list3);
# list.reverse()	倒排列表中的元素。
list3.reverse();
print("\tlist3.reverse():", list3)
# list.copy()	返回列表的浅复制，等于a[:]。
list4 = list3.copy();
print("\tlist4=list3.copy(),list4=", list4);
list4.append(list3);
list5 = list4.copy();
print("\tlist4.append(list3);list5 = list4.copy(),list5=", list5);

## 将列表当做堆栈使用LIFO关键函数pop()
print("将list5当做堆栈使用，输出list5元素关键函数list5.pop(),输出如下:")
while len(list5) > 0:
    print(list5.pop(), end=",")
print()

## 将列表当做队列使用FIFO关键函数popleft()
print("将list4当做队列使用，输出list4元素关键函数deque.popleft(),输出如下:")
deque1 = deque(list4)
while len(deque1) > 0:
    print(deque1.popleft(), end=",")
print()
## 列表推导式，列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，
# 用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
vec = [2, 4, 6]
vec2 = [4, 3, -9]
print("vec=", vec)
print("vec2=", vec2)
print("[x*3 for x in vec]=", [x * 3 for x in vec])
print("[[x, x**2] for x in vec]=", [[x, x ** 2] for x in vec])
print("[[x, x**2] for x in vec if x > 3 ]=", [[x, x ** 2] for x in vec if x > 3])
print("[x*y for x in vec for y in vec2]=", [x * y for x in vec for y in vec2])
print("[x+y for x in vec for y in vec2]=", [x + y for x in vec for y in vec2])
print("[vec[i]*vec2[i] for i in range(len(vec1))]=", [vec[i] * vec2[i] for i in range(len(vec))])
## 列表推导式可以使用复杂表达式或嵌套函数
print("[str(round(355/113, i)) for i in range(1, 6)]=", [str(round(355 / 113, i)) for i in range(1, 6)])
## 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print("matrix=", matrix)
print("[[row[i] for row in matrix] for i in range(4)]=", [[row[i] for row in matrix] for i in range(4)])
##del 语句,使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。
a = [-1, 1, 66.25, 333, 333, 1234.5]
print("a=", a)
del a[0];
print("after del a[0];a=", a)
del a[2:4];
print("after del a[2:4];a=", a)
del a[:];
print("after del a[:];a=", a)
# del a;print("after del a;a=", a) # del a后，a不存在，不同于del a[:]只是清空内部所有数据，本身还在只是为[]

"""
    descr:元组和序列,元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的
"""
t = 12345, 54321, 'hello!'
print("t=", t)
print("t[0]=", t[0])
u = t, (1, 2, 3, 4, 5)
print("u = t, (1, 2, 3, 4, 5);show u = ", u)

"""
    descr:集合,集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。可以用大括号({})创建集合。
        注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("basket ={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'},show basket=", basket)
print("'orange' in basket :", 'orange' in basket)
print("'oranges' in basket :", 'oranges' in basket)
## 集合间操作
set1 = set('abracadabra')
set2 = set('alacazam')
print("set1=", set1, ";set2=", set2)
print("在set1不在set2中的:set1-set2=", set1 - set2)
print("在set1或set2中的:set1|set2=", set1 | set2)
print("在set1且在set2中的:set1&set2=", set1 & set2)
print("当且仅当在set1或set2其中一个中的:set1^set2=", set1 ^ set2)
## 集合也支持推导式
collection1 = {x for x in 'abracadabra' if x not in 'abc'}
print("collection1 = {x for x in 'abracadabra' if x not in 'abc'},show collection1=", collection1)
"""
    descr:字典，理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
    序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
    一对大括号创建一个空的字典：{}。
"""
dict1 = {'jack': 4098, 'sape': 4139}
print("dict1=", dict1, ";dict1['jack']=", dict1['jack'])
## 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对
dict2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("dict2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]),show dict2=", dict2)
## 字典推导可以用来创建任意键和值的表达式词典
dict3 = {x: x ** 2 for x in (2, 4, 6)}
print("dict3={x: x**2 for x in (2, 4, 6)},show dict3=", dict3)
## 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便
dict4 = dict(sape=4139, guido=4127, jack=4098)
print("dict4 = dict(sape=4139, guido=4127, jack=4098),show dict4=", dict4)
"""
    descr:遍历技巧
"""
## 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print("knights=", knights)
print("""for k, v in knights.items():
    print("\t", k, v) """, "\n\t result:")
for k, v in knights.items():
    print("\t", k, v)
print()
## 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
print("""for i, v in enumerate(['tic', 'tac', 'toe']:
    print("\t", i, v) """, "\n\t result:")
for i, v in enumerate(['tic', 'tac', 'toe']):
    print("\t", i, v)
## 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print("questions=", questions, ";answers=", answers)
print("""for q, a in zip(questions, answers): 
    print("\tWhat is your {0}?  It is {1}.".format(q, a))""", "\n\t result:")
for q, a in zip(questions, answers):
    print("\tWhat is your {0}?  It is {1}.".format(q, a))
## 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
print("""for i in reversed(range(1, 10, 2)):
    print("\t", i)""", "\n\tresult:")
for i in reversed(range(1, 10, 2)):
    print("\t", i)
print()
## 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
print("""for f in sorted(set(basket)):
    print("\t", f)""", "\n\tresult:")
for f in sorted(basket):
    print("\t", f)
print()
print("basket=", basket)
