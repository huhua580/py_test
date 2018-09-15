#!/usr/bin/env python3
#coding:utf-8
def foo(arg):
    n = int(arg)
    if n == 0:
        raise ValueError('invalid value: %s' % arg)
    return 10 / n
def bar():
    try:
        foo('5')
    except ValueError as e:
        print('ValueError!')
        raise
print(bar())
