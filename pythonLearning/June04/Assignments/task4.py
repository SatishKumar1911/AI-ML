# Question 4: Descriptive Statistics with NumPy and SciPy
#
# Create a dataset with 20 random values between 1 and 100.
# Compute the following statistics for the dataset:
# Mean
# Median
# Standard deviation
# Variance
# Skewness
# Kurtosis

import numpy as np
from scipy import stats

dataset = np.random.randint(1, 100, 20)
print('Dataset:', dataset)

mean = np.mean(dataset)
print('Mean:', mean)

median = np.median(dataset)
print('Median:', median)

mode_result = stats.mode(dataset)
print(mode_result)

std = np.std(dataset)
print('Standard deviation:', std)

var = np.var(dataset)
print('Variance:', var)

skewness = stats.skew(dataset)
print('Skewness:', skewness)

kurtosis = stats.kurtosis(dataset)
print('Kurtosis:', kurtosis)