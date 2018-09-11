#!/usr/bin/env python3
#coding:utf-8
#s = [1, 2, 4, 5, 6, 9, 10, 15]
'''
s = range(1, 10)
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, s)))
'''
'''
s = ['a', 'b', 'c', None, 'd', '']
def not_empty(s):
    return s and s.strip()
print (list(filter(not_empty, s)))
'''
'''
print(sorted([38, 4, 34,-23,6,-2], key=abs))
'''
#i = [1, 3, 5, 7, 9]
def calc_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = calc_sum(1,3,5,6,8)
print(f())
