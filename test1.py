#!/usr/bin/env python3
#-------coding:utf-8------
'''
print('hello world')
'''
'''
str = '中文'.encode('utf-8')
bstr = str
print(str)
str = len(str)
print(str)
str = type(str)
print(str)

bstr = bstr.decode('utf-8')
print(bstr)
bstr = len(bstr)
print(bstr)
bstr = type(bstr)
print(bstr)
'''
'''
str = 'abc'.encode('utf-8')
print(str)
str = len(str)
print(str)
str = type(str)
print(str)

bstr = b'abc'.decode('utf-8')
print(bstr)
bstr = len(bstr)
print(bstr)
bstr = type(bstr)
print(bstr)
'''
'''
#格式化
name = input('请输入你的名字：')
age = int(input("请输入你的年龄："))
str = '你的名字是：%s \n你的年龄是：%d' %(name,age)
print(str)
'''
'''
s1 = 72
s2 = 85
score = (s2-s1)/72*100
str = '小明的成绩提升了：%.1f%%' %score
print(str)
'''
