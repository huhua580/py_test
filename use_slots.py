#!/usr/bin/env python3
#coding:utf-8
class Sutdent(object):
    __slots__ = ('name', 'age')

s = Sutdent()
s.name = 'Michael'
s.age = 29
s.score = 99
print(s.name)
print(s.age)
print(s.score)
