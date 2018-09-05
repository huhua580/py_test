#!/usr/bin/env python3
#=======coding:utf-8=====
import math
'''
n1 = 255
n1 = hex(n1)
print(n1)
n2 = 1000
n2 = hex(n2)
print(n2)
'''
'''
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-1))
'''
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
r = move(100, 100, 60, math.pi / 6)
print(type(r))
