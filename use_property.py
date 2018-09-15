#!/usr/bin/env python3
#coding:utf-8
'''
class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            print(ValueError('score must be an integer!'))
        if value < 0 or value > 100:
            print(ValueError('score must between 0~100!'))

        self.__score = value


bob = Student()
bob.score = 99
print(bob.score)
'''

class Screen(object):
    """docstring for Screen."""
    @property
    def wihth(self):
        return self.__w
    @wihth.setter
    def wihth(self, w):
        self.__w = w
    @property
    def height(self):
        return self.__h
    @height.setter
    def height(self, h):
        self.__h = h
    @property
    def resolution(self):
        return self.__w * self.__h

sd = Screen()
sd.wihth = 1024
sd.height = 768
print(sd.resolution)
