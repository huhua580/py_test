#!/usr/bin/env python3
#===coding:utf-8===
'''
l = [x * x for x in range(10)]
print(l)
g = (x * x for x in range(10))
for n in g:
    print(n)
'''
'''
def fib(max):
    n, a, b = 0, 0 ,1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'
fib(8)
'''
'''
def fib(max):
    n, a, b = 0, 0,1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    print('done')
for n in fib(8):
    print(n)
'''
for n in 'abcd':
    print(n)
