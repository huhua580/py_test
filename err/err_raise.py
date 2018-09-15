#!/usr/bin/env python3
#coding:utf-8
class FooError(ValueError):
    """docstring for FooError."""
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
print(foo('0'))
