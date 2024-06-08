# Question 1: Matrix Operations with NumPy
#
# Create two 3x3 matrices A and B with random integer values between 1 and 10.
# Compute the following:
# The sum of A and B.
# The difference between A and B.
# The element-wise product of A and B.
# The matrix product of A and B.
# The transpose of matrix A.
# The determinant of matrix A.

import numpy as np

A = np.random.randint(1, 10, size=(3, 3))
B = np.random.randint(1, 10, size=(3, 3))
print('A =')
print(A)
print()
print('B =')
print(B)

print('-'*30)

C = A + B
print('Addition of A and B is:')
print(C)

print('-'*30)

D = A - B
print('Subtraction of A and B is:')
print(D)

print('-'*30)

element_product = A * B
print('Element wise product of A and B is:')
print(element_product)

print('-'*30)

matrix_product = np.dot(A, B)
print('Matrix product of A and B is:')
print(matrix_product)

print('-'*30)

transpose_A = np.transpose(A)
print('Transpose of A is:')
print(transpose_A)

print('-'*30)

determinant_A = round(np.linalg.det(A))
print('Determinant of A is:')
print(determinant_A)
