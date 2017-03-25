#encoding=utf-8

# -*- coding: utf-8 -*-

# string
print '\nstring'
print'hello python',',duozijie'
print"I\'m lilei",'and age %s gender %d' % (25,True)
print'1+2=',1+2
#-  r'
print r'\\\t\\'
#- more lines
print '''line1
line2
line3'''
#input
print'please input your name :'
name = 'lilei'
#name = raw_input()
print'your name is ',name

# variable
print '\nvariable'
#-dynamic variable 
print '-dynamic variable'
a=123
print a 
b=a
a='abc'
print 'a=', a
print 'b=', b
print'\n\n'

# code
print 'code'
print 'A=', ord('A')
print '65=', chr(65)
print u"中文"

# list
print '\nlist'
list_classmate = ['lilei', "hanmeimei",'zhangliping']
print list_classmate,'len = ',len(list_classmate),',2nd= ',list_classmate[1]

list_classmate.append(123)
print list_classmate

list_classmate.insert(1,'Lily')
print list_classmate

list_classmate.pop(1)
print list_classmate
list_persion = ['jack',24]
print list_persion

list_classmate.insert(1,list_persion)
print list_classmate,'len = ',len(list_classmate)

# tuple
print '''\ntuple  
you can not modify it \n'''
tuple_classmate = ('lilei', "hanmeimei",list_classmate)
print tuple_classmate
list_classmate.pop(2)
print tuple_classmate


print list(range(5))

print list_classmate
print list_classmate[:2]
print list_classmate[-2:]

list_num = range(100)
print list_num
print list_num[3::10]

list_abc='abcdefghijklmn'
print list_abc[::3]


for ch in 'asdfghjkl;'[::2]:
	print ch

from collections import Iterable
print isinstance('abc', Iterable)
print isinstance(12345, Iterable)



for i, value in enumerate(['A', 'B', 'C']):
	print i, value



for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y
	
	
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
print L
g =(x * x for x in range(10))
print g
print next(g)
print next(g)
print next(g)




for n in g:
	print n,'in g'
	
	
#函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
	
fib(6)
#函数generator
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

	
g_fib = fib_g(6)

for n in g_fib:
	print n,'in g_fib'






