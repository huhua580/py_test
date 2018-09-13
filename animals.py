#!/usr/bin/env python3
#coding:utf-8
'''
class Animal(object):
    def run(self):
        print('Animal is running....')

class Cat(Animal):
    def run(self):
        print('I im cat')
class Dog(Animal):
    pass
class Tortoise(Animal):
    pass
    def run(self):
        print('Tortoise is running slowly.....')
'''
'''
a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
'''
'''
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Tortoise())
'''
'''
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(getattr(obj, 'z', 404))
'''

class Student(object):
    name = 'Student'

s = Student()
s.name = 'hunk'
del s.name
print(Student.name)
print(s.name)
