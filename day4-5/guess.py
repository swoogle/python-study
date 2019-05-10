#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

import random

secret = random.randint(1,100)
counter = 0
print('------猜数字游戏！-----')
guess = 0
while True:
    counter += 1
    guess = int(input('请输入数字：'))
    if guess < secret:
        print('您猜的数字小了！')
    elif guess > secret:
        print('您猜的数字大了！')
    else:
        print('恭喜，您猜对了！')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足！')