#encoding=utf-8

# -*- coding: utf-8 -*-


print max(1,2)
print'max(1,2) = ',max(1,2)

print 'int(\'123\')=',int('123')


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

		

print my_abs(2)
print my_abs(-2)

def sum2N(n):
	sum = 0
	for x in range(n):
		sum = sum + x
	return sum
	

print sum2N(101)


def llshpower(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
	
print '2^10=', llshpower(2,10)

print '2^ =', llshpower(2)


def lllshadd_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
	


llshlist = range(10)
print lllshadd_end(llshlist)

llshlist_none = None
print lllshadd_end(llshlist_none)



def llshcalc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
	
	
print llshcalc(1,4,100) 


nums = [1, 2, 3]
print llshcalc(*nums) 



print 'function  map'
def f(x):
	return x * x

print  map(f, range(9))
print  map(str, range(9))



def fn(x, y):
	return 10*x + y

	
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
	
	
print str2int('3242315')