#!/usr/bin/env python3
#coding:utf-8
'''
def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    return r
def bar():
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass
'''
'''
try:
    print('try....')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally')
print('END')
'''
'''
try:
    print('try....')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally....')
print('END')
'''
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        return bar('5')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
ma = main()
print(ma)
