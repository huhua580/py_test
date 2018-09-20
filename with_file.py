#!/usr/bin/env python3
#coding:utf-8
'''
try:
    f = open('/home/hh/pytest/with_file.txt', 'r')
    print(f.read())
finally:
    if f:
    f.close()
'''
'''
with open('/home/hh/pytest/with_file.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())
'''
'''
with open('/home/hh/pytest/timg.jpeg','rb') as f:
    print(f.read())
'''
f = open('/home/hh/pytest/with_file.txt', 'w')
f.write('hello yimo')
f.close()
