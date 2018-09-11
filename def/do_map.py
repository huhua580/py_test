#!/usr/bin/env python3
#coding:utf-8
'''
from functools import reduce
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print(list(map(str,[1, 2, 3, 4, 5, 6, 7, 8, 9])))

def add(x, y):
    return x + y

sum = reduce(add, [1, 3, 5, 7, 9])
print(sum)
'''
'''
def f(x):
    return x * x
m = map(f, range(1,10))
print (list(m))
'''
st = map(str, range(1, 10))
print(list(st))
