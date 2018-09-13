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
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' %(self.name, self.score))

bob = Student('bob', 81)
lisa = Student('Lisa Simpson', 85)
bob.print_score()
lisa.print_score()
