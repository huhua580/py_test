#! /usr/bin/env python3
#========coding:utf-8==========
'''
def power(x,n=2):
    s = 1
    while n > 0:
        s = s *x
        n = n -1
    return s
print(power(5, 6))
'''
'''
def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l
print(add_end([1, 2, 3]))
'''
'''
def calc(*num):
    sum = 0
    for n in num:
        sum = sum + n *n
    return sum
print(calc())
'''
'''
def person(name, age, **k):
    print("name:", name, "age:", age, k)
extra = {'city':'beijing', 'job':'engineer'}
person('jack', 25,**extra)
'''
'''
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
print('=============================')
f2(1, 2, d=99)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3, 4)
kw = {'d' : 99, 'x' : '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d' : 99, 'x' : '#'}
f2(*args, **kw)
'''
'''
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)

print(fact(800))
'''
def move(n, a, b, c):
    if(n == 1):
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
