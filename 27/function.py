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
		print(x)
		sum = sum + x
	return sum
	

print sum2N(101)