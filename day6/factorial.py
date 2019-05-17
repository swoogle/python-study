#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

# 将求阶乘的功能封装成一个函数
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result

if __name__ == '__main__':
    print(factorial(7) // factorial(3) // factorial(4))