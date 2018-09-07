import os #导入os模块
#!/usr/bin/env python3
#===coding:utf-8===

#print('hello world')
'''
ls = [x * x for x in range(1, 11) if x % 2 == 0]
print(ls)
ls1 = [m + n for m in 'ABC' for n in 'XYZ']
print(ls1)
'''
'''
test = [d for d in os.listdir('.')]
print(test)
'''
'''
d = {'x':'a', 'y':'b', 'z':'c'}
dl = [k + '=' + v for k, v in d.items()]
print(dl)
'''
'''
l = ['Hello', 'World', 'IBM', 'Apple']
ls = [s.lower() for s in l]
print(ls)
'''
l = ['Hello', 'world', 18, 'IBM', 'Apple', None]
ls = [s.lower() for s in l if isinstance(s, str)]
print(ls)
