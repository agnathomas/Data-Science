#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:47:13 2021

@author: sjcet
"""

import numpy as np
import numpy as nf
from numpy.linalg import eig
mat = np.random.randint(10, size=(3, 3))
array = nf.random.randint(10, size=(3, 3))
print("Square matrix \n",mat)

M_inverse = np.linalg.inv(mat)
print("Inverse of the matrix\n",M_inverse)

rank = np.linalg.matrix_rank(mat)
print("Rank of the given Matrix \n",rank)

det= np.linalg.det(mat)
print("Determinant of the given Matrix \n",det)

arr=mat.flatten()
print("Transform matrix to 1D array \n",arr)

w,v=eig(array)
print('Eigen value \n', w)
print('Eigen vector \n', v)