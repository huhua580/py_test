#!/usr/bin/env python3
#coding:utf-8
'''
try:
    f = open('/home/hh/pythonpj/io/test.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
'''
f = open('/home/hh/pythonpj/io/test.txt','r')
with f as fr:
    print(fr.read())
