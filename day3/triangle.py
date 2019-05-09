#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and b + c > a and a + c > b:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c)) # 海伦公式
    print('面积: %f' % (area))
else:
    print('不能构成三角形')