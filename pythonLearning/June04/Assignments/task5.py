# Question 5: Hypothesis Testing with SciPy
# Generate a sample dataset of 30 random values from a normal distribution with mean 50 and standard deviation 5.
# Perform a one-sample t-test to check if the sample mean is significantly different from 50.

import numpy as np
from scipy.stats import ttest_1samp

mean = 50
std_dev = 5
sample_size = 30

np.random.seed(0)
dataset = np.random.normal(mean, std_dev, sample_size)
print('Dataset:\n', dataset)
print()

population_mean = 50
alpha = 0.05

# H0: No significant difference between sample mean and population mean
# H1: Significant difference between sample mean and population mean

t_statistic, p_value = ttest_1samp(dataset, population_mean)
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
print()
if p_value < alpha:
    print('Reject the null hypothesis: The sample mean is significantly different from the population mean.')
else:
    print('Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.')
