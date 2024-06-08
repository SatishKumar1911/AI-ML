# Question 2: Solving Linear Equations with SciPy
#
# Given the system of equations:
# 2x + 3y = 8
# 3x + 4y = 11
#
# Represent the system of equations in matrix form AX = B.
# Use scipy.linalg.solve to find the values of x and y.

import numpy as np
from scipy import linalg

A = np.array([[2, 3], [3, 4]])
B = np.array([8, 11])

x = linalg.solve(A, B)

print('For the equation:\n\n2x + 3y = 8\n3x + 4y = 11')
print(f'Value of x = {x[0]}')
print(f'Value of y = {x[1]}\n')

print(f'Cross checking: {np.dot(A, x) == B}')

