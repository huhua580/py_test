import math
#!/usr/bin/env python3
#=======coding:utf-8=====

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
'''
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
r = move(100, 100, 60, math.pi / 6)
print(type(r))
'''

def quadratic(a, b, c):
    if a == 0:
        return 'a不能为零'
    else:
        sum = b**2-4*a*c
        if sum < 0:
            str = '原方程无实根'
            return str
        elif sum == 0:
            x = -b/(2*a)
            return x
        elif sum > 0:
            x1 = (-b+math.sqrt(sum))/(2*a)
            x2 = (-b-math.sqrt(sum))/(2*a)
            return x1, x2


print(quadratic(0,1, -1))
