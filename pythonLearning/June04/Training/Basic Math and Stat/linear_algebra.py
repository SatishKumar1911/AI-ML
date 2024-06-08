# Importing numpy package
import numpy as np

print('-'*30)

# Creating vectors
vector_2d = np.array([1, 2])  # x, y
vector_3d = np.array([3, 4, 5])  # x, y, z

# Printing the type of vector
print('Type of vector:', type(vector_2d))

# Printing vectors
print('2D vector:', vector_2d)
print('3D vector:', vector_3d)

print('-'*30)

# Creating vector A and B to perform Addition & Subtraction
A = np.array([1, 2])
B = np.array([3, 4])

print('A:', A)
print('B:', B)

# Addition
add = A + B  # [A1 + B1, A2 + B2]
print('Add:', add)

# Subtraction
sub = A - B  # [A1 - B1, A2 - B2]
print('Sub:', sub)

print('-'*30)

# Scalar multiplication with vector
scalar = 3
vector = np.array([1, 2])
scalarXvector = scalar * vector

print('Scalar:', scalar)
print('Vector:', vector)
print('Scalar * Vector:', scalarXvector)

print('-'*30)

# Dot product
vector_a = np.array([1, 2])
vector_b = np.array([3, 4])
dot_product = np.dot(vector_a, vector_b)
print('A:', vector_a)
print('B:', vector_b)
print('Dot product', dot_product)

# Magnitude of vectors
magnitude_a = np.linalg.norm(vector_a)
magnitude_b = np.linalg.norm(vector_b)

# Cosine angle between A and B
cos_theta = dot_product / (magnitude_a * magnitude_b)

# Find angle is acute or obtuse

# 