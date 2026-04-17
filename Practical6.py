# Practical 6: t-test, normal test, F-test

import numpy as np
from scipy import stats

# -------------------------------
# 1. One Sample t-test
# -------------------------------
data = np.array([72, 68, 75, 70, 69, 71, 73, 74, 67])
mu0 = 70.8

t_stat, p_val = stats.ttest_1samp(data, mu0)

print("T-test:")
print("t-stat =", t_stat)
print("p-value =", p_val)


# -------------------------------
# 2. Normality Test (Shapiro Test)
# -------------------------------
stat, p = stats.shapiro(data)

print("\nNormality Test:")
print("p-value =", p)


# -------------------------------
# 3. Independent t-test
# -------------------------------
group1 = np.array([20, 22, 19, 24, 21])
group2 = np.array([18, 17, 20, 16, 19])

t_stat, p_val = stats.ttest_ind(group1, group2)

print("\nIndependent T-test:")
print("p-value =", p_val)


# -------------------------------
# 4. F-test (Variance Test)
# -------------------------------
var1 = np.var(group1, ddof=1)
var2 = np.var(group2, ddof=1)

f_stat = var1 / var2
print("\nF-test:")
print("F-stat =", f_stat)
