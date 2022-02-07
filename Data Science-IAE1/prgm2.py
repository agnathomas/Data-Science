#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:24:33 2022

@author: sjcet
"""

import numpy as np
a=np.arange(1,21,1,dtype=float)
print("1D array with 20 elements:\n",a)

b=np.arange(1,20*2,2)
print("Odd Array : ",b)

c=b.reshape(5,4)
print("Reshape array to 5x4 matrix:\n",c)


print("Display the elements of rows 2 to 5 and columns 1 to 3:")
print(c[1:5 , 0:3])

print("Display the elements of 2nd and 3rd column:")
print(c[:,1:3])

d=c[-1]
print("Last row:",d)
print("Display last 2 elements of last row:")
print(d[-2:])
