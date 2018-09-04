#!/usr/bin/env python3
#=======coding:utf-8=========
'''
print('hello world!')
'''
'''
classmates = ('Michael', 'Bob', 'Tracy',123)
print(classmates)
print(type(classmates))
print(len(classmates),'\n==============')
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[3])
print(classmates[-1], '\n===============')
'''
'''
t = ('a', 'b', ['A', 'B'])
print(t,'\n==================')
t[2][0] = 'Y'
t[2][1] = 'N'
print(t)
'''
l1 = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
#打印APPLE
print('APPLE:', l1[0][0], '\n======')
#打印PYTHON
print('PYTHON:',l1[1][1], '\n======')
#打印LISA
print('LISA:', l1[2][2], '\n======')
