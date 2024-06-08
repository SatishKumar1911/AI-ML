# Exercise 2: Perform Basic and Advanced Array Operations
#
# a. Array arithmetic:
# Create two 1-dimensional arrays of integers from 1 to 5 and 6 to 10.
# Perform element-wise addition, subtraction, multiplication, and division and Print the results.
#
# b. Indexing and slicing:
# Create a 5x5 array with values from 1 to 25.
# Extract the subarray consisting of the first two rows and columns.
# Print the extracted subarray.
#
# c. Boolean indexing:
# Create a 1-dimensional array of integers from 10 to 19.
# Extract elements greater than 15.
# Print the resulting array.

import numpy as np

# a. Array arithmetic:
array1_1d = np.arange(1, 5)
array2_1d = np.arange(6, 10)
print('array1_1d\n', array1_1d)
print('array2_1d\n', array2_1d)
print()

# Element-wise addition
print("Element-wise addition:", array1_1d + array2_1d)

# Element-wise subtraction
print("Element-wise subtraction:", array1_1d - array2_1d)

# Element-wise multiplication
print("Element-wise multiplication:", array1_1d * array2_1d)

# Element-wise division
print("Element-wise division:", array1_1d / array2_1d)
print()


# b. Indexing and slicing:
# Create a 5x5 array with values from 1 to 25.
array_2d = np.arange(1, 26).reshape(5, 5)
print('2-dimensional\n', array_2d)
print('Shape:', array_2d.shape)
print()

# Extract the subarray consisting of the first two rows and columns.
extracted_array = array_2d[0:2, 0:2]
print('Extracted sub array:\n', extracted_array)
print()

# c. Boolean indexing:
# Create a 1-dimensional array of integers from 10 to 19.
array = np.arange(10, 19)
print('1-dimensional\n', array)
# Extract elements greater than 15.
result = array[array > 15]
print('Extract elements\n', result)
