# Exercise 3: Use NumPy for Mathematical and Statistical Calculations
import numpy as np

# a. Mathematical functions:
# Create an array of 10 evenly spaced values between 0 and 2π.
array_1d = np.linspace(0, 2*np.pi, 10)
print('array:\n', array_1d)
print()

# Compute the sine, cosine, and tangent of each value.
sine = np.sin(array_1d)
cosine = np.cos(array_1d)
tangent = np.tan(array_1d)

# Print the results.
print('sine:\n', sine)
print()
print('cosine:\n', cosine)
print()
print('tangent:\n', tangent)
print()

#
# b. Statistical functions:
# Create a 3x3 array with random integers between 1 and 100.
array_2d = np.random.randint(1, 100, (3, 3))
print('array_2d:\n', array_2d)
print()
# Compute the mean, median, standard deviation, and variance.
mean = np.mean(array_2d)
median = np.median(array_2d)
std_dev = np.std(array_2d)
var = np.var(array_2d)

# Print the results.
print('mean:\n', mean)
print('median:\n', median)
print('standard deviation:\n', std_dev)
print('variance:\n', var)
