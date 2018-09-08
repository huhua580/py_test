#!/usr/bin/env python3
#coding:utf-8
from functools import reduce
'''
def add(x, y):
    return x + y
def fn(x, y):
    return x *10 + y
re = reduce(fn, range(1, 5))
print(re)
'''
'''
def fn(x, y):
    return x * 10 + y
def char2num(s):
    digits = {'0':0, '1':1, '2':2,'3':3, '4':4, '5':5, '6':6, '7':7,'8':8, '9':9}
    return digits[s]

nt = reduce(fn, map(char2num, '13579'))

print(nt)
'''
'''
digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num, s) )
print(str2int('13579'))
'''
'''
digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2num(s):
    return digits[s]
def str2int(s):
    return reduce(lambda x,y: x * 10 + y, map(char2num, s))
print(str2int('13579'))
'''
def normalize(name):
    return name.capitalize()
l1 = ['adam', 'LISA','barT']
l2 = list(map(normalize, l1))
print(l2)
