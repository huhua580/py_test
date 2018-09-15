#!/usr/bin/env python3
#coding:utf-8
'''
class Student(object):
    """docstring for Student."""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return('Student object (name: %s)' %self.name)
    __repr__ = __str__
s = Student('Michael')
print(s)
'''
'''
class Fib(object):
    """docstring for Fib."""
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b  = self.b, self.a + self.b
        if self.a > 10:
            return StopIteration()
        return self.a

for n in Fib():
    print(n)
'''
