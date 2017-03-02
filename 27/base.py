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
list_classmate = ['lilei', "hanmeimei"]
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


