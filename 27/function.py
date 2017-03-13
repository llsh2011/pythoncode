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
