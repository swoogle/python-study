#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

"""
输出斐波那契数列的前100个数
"""

a = 0
b = 1
for _ in range(100):
    (a, b) = (b, a + b)
    print(a, end=' ')