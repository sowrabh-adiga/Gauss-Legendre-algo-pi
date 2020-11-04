# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:53:23 2020

@author: sowrabh adiga
"""
import time
t0 = time.time()  # to measure execution time

from decimal import *  #better than float


getcontext().prec = 100000  #print 100 thousand decimal places of pi

#---------------- Algorithm -------------------------#
a = 1
b = Decimal(1) / Decimal(2).sqrt()
t = Decimal(1) / Decimal(4)
p = 1

for _ in range(25):
	an = (a + b) / 2
	b = (a * b).sqrt()
	t -= p * (a - an) ** 2
	p *= 2
	a = an

data = ((a + b) ** 2) / (4 * t)

#---------------- Algorithm -------------------------#

# print to a file
f = open("piValue100000.txt", "w")
f.write(str(data))
f.close()

#print time required for execution
print("--- %s seconds ---" % (time.time() - t0))








