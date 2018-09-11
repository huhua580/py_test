#!/usr/bin/env python3
#========coding:utf-8=============
'''
#names = ['Michael', 'Bob', 'Tracy']
#scores = [95, 75, 85]
d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}
#print(d['Michael'])
d['Tracy'] = 65
#print(d['Tracy'])
d['Jack'] = 90
#print(d['Jack'])
d.get('Thomas', 411)
d.pop('Bob')

for x in d:
    print(x,' = ', d[x])
'''
'''
s = set([1, 2, 3, 3, 3])
s.add(4)
s.remove(4)
print(s)
'''
s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])
print(s1 | s2)
print(s1 & s2)
