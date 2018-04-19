#!/usr/bin/env python3
"""
    descr:斐波那契数列实现
"""
a, b = 0, 1
while b < 1000:
    print(b, end=",")
    a, b = b, a + b
print()
print(pow(2, 6))
