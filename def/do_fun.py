#!/usr/bin/env python3
#coding:utf-8
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))
