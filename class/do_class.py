#/usr/bin/env python3
#coding:utf-8

#这是面向过程的写法
'''
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

std1 = {'name':'bob', 'score':81}
std2 = {'name': 'Michael', 'score':98}
print_score(std2)
'''
#这是面向对象的写法
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_scoer(self):
        return self.__score
    def set_scoer(self, scoer):
        if 0 <= scoer <= 100:
            self.__score = scoer
        else:
            print('bad score')

    def print_score(self):
        print('%s : %s' %(self.__name, self.__score))

bob = Student('bob', 81)
lisa = Student('Lisa Simpson', 85)

bob.print_score()
lisa.print_score()
