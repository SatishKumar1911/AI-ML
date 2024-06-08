import numpy as np
import numba
import time


# a. Vectorization:
# Create a function to compute the element-wise square of an array using a for loop.
def square(arr):
    result = np.zeros_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result


# Create another function to perform the same computation using NumPy vectorization.
def square_vectorized(arr):
    return arr ** 2


# b. Numba:
# Use the @numba.jit decorator to optimize the function from step 1 that uses a for loop.
@numba.jit(nopython=True)
def square_numba(arr):
    result = np.zeros_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result


# Compare the performance of the three functions using a large array of size 1,000,000.
array = np.random.randint(1, 1000, size=1_000_000)

# Measure the time taken by the square function
start_time = time.time()
by_square = square(array)
end_time = time.time()
print('Square function time taken:', end_time - start_time, 'seconds')

# Measure the time taken by the square_vectorized function
start_time = time.time()
by_square_vectorized = square_vectorized(array)
end_time = time.time()
print('Vectorized function time taken:', end_time - start_time, 'seconds')

# Measure the time taken by the square_numba function
start_time = time.time()
by_square_numba = square_numba(array)
end_time = time.time()
print('Numba-optimized function time taken:', end_time - start_time, 'seconds')

# Verify that all methods produce the same result
assert np.array_equal(by_square, by_square_vectorized)
assert np.array_equal(by_square_vectorized, by_square_numba)

print("All methods produce the same result.")
