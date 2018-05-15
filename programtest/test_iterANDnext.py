#!/usr/bin/env python3

"""
    descr:迭代器与生成器,主要值iter和next
"""


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while counter <= n:
        yield a
        a, b = b, a + b
        counter += 1


pass

if __name__ == "__main__":
    languages = ["C", "C++", "JAVA", "Python", "Perl", "Go"]
    it = iter(languages)
    print(next(it), next(it), next(it), next(it))

    while True:
        try:
            print(next(it), end=" ")
        except StopIteration:
            break
    else:
        print("不可能正常执行完")

    pass
    print()
    it = iter(languages)
    for o in it:
        print(o, end=" ")
    else:
        print("\n正常执行完")

    """
        descr:生成器,使用了 yield 的函数被称为生成器,返回值能够直接得到一个迭代器
    """
    # f 是一个迭代器，由生成器返回生成
    f = fibonacci(10)
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            break
else:
    print("外部调用：__name__=", __name__)
