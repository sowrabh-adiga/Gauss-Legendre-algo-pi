# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:53:23 2020

@author: sowra
"""
import time
t0 = time.time()

from decimal import *


getcontext().prec = 100000

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

#print (((a + b) ** 2) / (4 * t))
data = ((a + b) ** 2) / (4 * t)
f = open("piValue100000.txt", "w")
f.write(str(data))
f.close()

print("--- %s seconds ---" % (time.time() - t0))








