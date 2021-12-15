#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:57:54 2021

@author: sjcet
"""

import numpy as np
mat =np.array([[1, 2, 3],[3,2,4],[2,2,1]])
print("Matrix is....\n",mat)

print("Cubes using *")
print(mat*mat*mat)

print("Cubes using **")
print(mat**3)
  
print("Cubes using multiply()")
print(np.multiply(mat,(mat*mat)))

print("Cubes using power()")
print(np.power(mat,3))
print(pow(mat, 3))


b = np.identity(3, dtype = int)
print("Identity matrix:\n", b)

out = np.power(mat, mat)
print("Each element of the matrix to different powers:\n",out)

x = np.arange(1,10).reshape(3,3)
y = np.arange(11,20).reshape(3,3)
print("matrix x \n", x ,"\n Matrix y\n",y)
print("perform the operation X^2 +2Y: \n",np.add((np.power(x,2)),(np.multiply(y,2))))