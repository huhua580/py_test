#!/usr/bin/env python3
#--------coding:utf-8---------
'''
print('hello world!')
'''
'''
str = 'Holle 中国！'
bstr = str.encode('utf-8')
print(bstr)
print(type(bstr),'\n====================')
str1 = bstr.decode('utf-8')
print(str1)
print(type(str1))
'''
'''
classmates = ['Michael','Bob','Tracy']
print('列表内容：',classmates,'\n===========')
print('数据类型：',type(classmates),'\n===============')
print('元素个数：',len(classmates),'\n===============')
print('元素索引内容：', classmates[0])
print('元素索引内容：', classmates[1])
print('元素索引内容：', classmates[2])
print('==================================')
#print(classmates[-1])
classmates.append('Adam')
classmates.insert(1,'Jack')
classmates.pop()
classmates.pop(1)
classmates[1] = 'Sarah'
print(classmates)
'''
l = ['Apple', 123, True]
print(l)
s = ['python', 'java',['asp', 'php'], 'scheme']
s[2][0] = 'jsp'
s[2].append('hunk')
s[2].insert(1, 'huha')
s[2].pop()
s[2].pop(1)
print(s)
print(len(s))
l1 = []
print('l1变量：%s' %len(l1))
