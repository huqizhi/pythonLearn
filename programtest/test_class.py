#! /usr/bin/env python3
"""
    descr: Python3 面向对象
    1、类用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。相关概念理解：
        1.1、类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用；
        1.2、实例变量：定义在方法中的变量，只作用于当前实例的类；
        1.3、方法：类中定义的函数；
        1.4、数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据；
        1.5、父类和子类关系为派生和继承，子类可当做父类来对待。子类天然继承父类所有东西，而且子类可以扩展变更处理。
            如果子类重新实现了继承而来方法，叫做方法重写。如果子类实现了父类以外的东西叫拓展。
        1.6、创建一个类的实例，类的具体对象，这叫做实例化。
        1.7、实例化的东西(通过类定义的数据结构来构造出来的东西)叫对象。
    2.类定义，相关东西：（实例本身惯例参数名是self，当然也可以是其他）
        2.1、构造函数 __init__(self[,param1,param2...])，可以有参数，但第一个一定表示实例本身；
        2.2、方法  fn(self[,param1,param2...])，可以有参数，但第一个一定表示实例本身,这也是类方法区别于非类方法的地方；
        2.3、打印实例的方法 __str__(self[,param1,param2...])，可以有参数，但第一个一定表示实例本身；
        2.4、析构函数__del__(self[,param1,param2...])，释放对象时使用；
        2.5、类多继承时，如果没有重写方法，方法调用将在父类中从左到右查找第一个匹配的既是；
        2.6、私有属性命名规范为__attribute，不能在类地外部被使用或直接访问;
        2.7、私有方法命名规范为__function，不能在类地外部被使用;
        2.8、类的专有方法有：
            __init__ : 构造函数，在生成对象时调用；
            __del__ : 析构函数，释放对象时使用；
            __repr__ : 打印，转换；
            __setitem__ : 按照索引赋值；
            __getitem__: 按照索引获取值；
            __len__: 获得长度；
            __cmp__: 比较运算；
            __call__: 函数调用；
            __add__: 加运算；
            __sub__: 减运算；
            __mul__: 乘运算；
            __div__: 除运算；
            __mod__: 求余运算；
            __pow__: 乘方；
            __str__: 实例转化为字符串的方法，默认打印类和地址，类似<__main__.people object at 0x00000272A730D278>
        2.9、四则运算的支持，对上面类的专有方法中运算方法实现即可；自定义类里若没有实现直接使用则会报错；
"""


class Animal:
    __instants = 0
    name = '动物'
    age = 8

    def __init__(self, name, age):
        Animal.__instants += 1
        self.__instants += 1
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def prt(self):
        print("in Animal")
        print(self)
        print(self.__class__)

    def __getCount(self):
        return Animal.__instants

    def getCount(self, isBase=False):
        if isBase:
            return Animal.__instants
        else:
            return self.__instants


pass


class Dog(Animal):
    isHuzhu = False

    def __init__(self, name, age, isHuzhu):
        ## 调用父类的__init__方法才会触发父类的初始化
        Animal.__init__(self, name, age)
        ## 不调用父类的__init__方法不会触发父类的初始化
        # self.name = name
        # self.age = age
        self.isHuzhu = isHuzhu

    def prt(self):
        print("in Dog")
        print("Dog【{}】今年{}岁护主:{}".format(self.name, self.age, self.isHuzhu))

    pass


pass


class Panda(Animal):
    isLovely = True

    def __init__(self, name, age, isLovely):
        Animal.__init__(self, name, age)
        self.isLovely = isLovely

    def prt(self):
        print("in Dog")
        print("Panda【{}】今年{}岁,可爱啊:{}".format(self.name, self.age, self.isLovely))

    pass


pass


class Cat(Animal):
    isCatchmice = True

    def __init__(self, name, age, isCatchmice=True):
        Animal.__init__(self, name, age)
        self.isCatchmice = isCatchmice

    def prt(self):
        print("in Cat")
        print("Cat【{}】今年{}岁,它抓老鼠:{}".format(self.name, self.age, self.isCatchmice))

    pass


pass


class CatDog(Cat, Dog):
    def __init__(self, name, age, isHuZhu, isCatchMice):
        Cat.__init__(self, name, age, isCatchMice)
        self.isHuzhu = isHuZhu

    pass


pass


class AlienSpecies(Cat, Dog, Panda):
    def __init__(self, name, age, isHuZhu=True, isCatchMice=True, isLovely=True):
        Panda.__init__(self, name, age, isLovely)
        self.isHuzhu = isHuZhu
        self.isCatchmice = isCatchMice

    pass


pass


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 实例打印方法重载
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    # 加法重载
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


if __name__ == "__main__":
    dog = Dog("旺财", 6, True)
    # 调用子类方法
    dog.prt()
    # 调用父类方法
    # super(Dog, dog).prt()
    print("Animal实例数:", dog.getCount())
    print("==============")
    cat = Cat("喵喵", 2)
    # 调用子类方法
    cat.prt()
    # 调用父类方法
    # super(Cat, cat).prt()
    print("Animal实例数:", cat.getCount())
    print("==============")
    catDog = CatDog("狗喵新品种", 20, True, True)
    # 默认调用第一个父类方法
    catDog.prt()
    # 指定调用某父类的父类方法
    super(Dog, catDog).prt()
    # 指定调用当前类的父类方法--这里调用了第一个父类方法--同默认
    super(CatDog, catDog).prt()
    print("Animal实例数:", catDog.getCount())
    print("==============")
    alienSpecies = AlienSpecies("外星物种", 2081, True, True)
    # 默认调用第一个父类方法
    alienSpecies.prt()
    # 指定调用某父类的父类方法
    super(Panda, alienSpecies).prt()
    # 指定调用当前类的父类方法--这里调用了第一个父类方法--同默认
    super(AlienSpecies, alienSpecies).prt()
    print("Animal实例数:", alienSpecies.getCount(True))
    print("Animal实例数:", alienSpecies.getCount(False))

    ## 加法运算重载了，可以相加啦
    v1 = Vector(2, 5)
    v2 = Vector(3, 7)
    print("v1={},v2={},v1+v2={}".format(v1, v2, v1 + v2))
    print("v1-v2={}".format(v1 - v2))
