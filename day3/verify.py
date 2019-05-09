#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

"""
用户身份验证
"""
import getpass

username = input('请输入用户名：')
password = getpass.getpass('请输入口令: ')
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')