# Question 2: Two-Sample t-Test
# Perform a two-sample t-test to compare the means of two independent samples.
#
# Generate two sample datasets each with 25 random values from normal distributions with means of 55 and 60,
# and a standard deviation of 8. Perform an independent two-sample t-test to check if the means of the two samples
# are significantly different.

import numpy as np
from scipy.stats import ttest_ind

mean1 = 55
mean2 = 60
std_dev = 8
sample_size = 25

np.random.seed(0)
dataset1 = np.random.normal(mean1, std_dev, sample_size)
dataset2 = np.random.normal(mean2, std_dev, sample_size)

print('Dataset1:\n', dataset1)
print()
print('Dataset2:\n', dataset2)
print()

# H0: No significant difference
# H1: Significant difference

t_statistics, p_values = ttest_ind(dataset1, dataset2)
alpha = 0.05
print(f"T-statistic: {t_statistics}")
print(f"P-value: {p_values}")
print()

if p_values < alpha:
    print('Reject the null hypothesis: The means of the two samples are significantly different.')
else:
    print('Fail to reject the null hypothesis: The means of the two samples are not significantly different.')
