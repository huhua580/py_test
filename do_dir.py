#!/usr/bin/env python3
#coding:utf-8
import os
#print(os.uname())
#print(os.environ)
#print(os.path.abspath('.'))
#print(os.path.join('/home/hh/pytest', 'test'))
#os.mkdir('/home/hh/pytest/test')
#os.rmdir('/home/hh/pytest/test')
di = [x for x in os.listdir('.') if os.path.isdir(x)]
print(di)
fi = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(fi)
