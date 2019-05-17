#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

os.chdir('/Users/cocoon')
os.system('ls -l')
os.mkdir('test')
shutil.copy('/Users/cocoon/c.png', '/Users/cocoon/test/cc.png')


def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % kw['name'])
    if 'tel' in kw:
        print('你的联系电话是: %s!' % kw['tel'])
    if 'age' in kw:
        print('你的年龄是: %d!' % kw['age'])


param = {'name': '骆昊', 'age': 38}
f3(**param)
f3(name='骆昊', age=38, tel='13866778899')
f3(user='骆昊1', age=39, tel='13866778898')
f3(user='骆昊2', age=40, mobile='13866778897')