#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
"""
x = int(input('请输入一个正整数: '))
t = x
y = 0
while t > 0:
    y = y * 10 + t % 10
    t //= 10
if x == y:
    print('%d是回文数' % x)
else:
    print('%d不是回文数' % x)