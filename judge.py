#!/usr/bin/env python3
#=======coding:utf-8==========
'''
age = int(input('输入您的年龄：'))
if age >=18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is',age)
    print('teenager')
else:
    print('kid')
'''
'''
s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
'''
#判断语句练习
height = 1.75
weight = 70.5
bmi = round(weight/(height**2))
if bmi < 18.5:
    print('您的体重过轻')
elif 18.5 >= bmi <= 25:
    print('您的体重正常')
elif 25 >= bmi <= 28:
    print('您的体重过重')
elif 28 >= bmi <= 32:
    print('您的体重肥胖')
elif bmi < 32:
    print('您的体重严重肥胖')
