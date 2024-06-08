# Exercise 1: Create different types of NumPy arrays and perform basic manipulations.
#
# a. Create a 1-dimensional array:
# Create a 1-dimensional array of integers from 0 to 9.
# Print the array and its shape.
#
# b. Create a 2-dimensional array:
# Create a 2-dimensional array (3x3) with values from 1 to 9.
# Print the array, its shape, and the sum of all elements.
#
# c. Reshape the array:
# Reshape the 1-dimensional array from step 1 into a 2x5 array.
# Print the reshaped array and its shape.

import numpy as np

# a. Create a 1-dimensional array:
array_1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print('1-dimensional\n', array_1d)
print('Shape:', array_1d.shape)
print()

# b. Create a 2-dimensional array:
array_2d = np.array([[1, 2, 3], [4, 5, 6], [8, 9, 10]])
print('2-dimensional\n', array_2d)
print('Shape:', array_2d.shape)
print()

# c. Reshape the array
reshaped_array = array_1d.reshape(2, 5)
print('Reshaped\n', reshaped_array)
print('Shape:', reshaped_array.shape)
