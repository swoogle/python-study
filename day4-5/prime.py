#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

"""
输出1000以内的素数
"""
from math import sqrt

for num in range(1, 1000):
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print(num, end=' ')