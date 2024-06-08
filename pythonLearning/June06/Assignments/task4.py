# Exercise 4: Implement Broadcasting and Vectorized Operations
import numpy as np
import time
# a. Broadcasting:
# Create a 3x1 array with values from 1 to 3.
array1 = np.arange(1, 4).reshape(3, 1)
print(array1)
print()

# Create a 1x3 array with values from 4 to 6.
array2 = [4, 5, 6]
print(array2)
print()

# Add the two arrays using broadcasting.
array3 = array1 + array2
# Print the resulting array.
print(array3)
print()


# b. Vectorized operations:
# Create two large arrays of size 1,000,000 with random values.
array_one = np.random.randint(1, 1000, size=1_000_000)
array_two = np.random.randint(1, 1000, size=1_000_000)
print('array_one:', array_one)
print('array_two:', array_two)
print()

# Compute the element-wise product of the two arrays.
start_time = time.time()
array_three = array_one * array_two
end_time = time.time()
time_taken = end_time - start_time

# Print the time taken for the computation using vectorized operations.
print('Time taken:', time_taken, 'seconds')
