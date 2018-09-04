#!/usr/bin/env python3
#========coding:utf-8=============

#names = ['Michael', 'Bob', 'Tracy']
#scores = [95, 75, 85]
d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}
#print(d['Michael'])
d['Tracy'] = 65
#print(d['Tracy'])
d['Jack'] = 90
#print(d['Jack'])

for x in d:

    print(x, '的成绩是：',d[x])
