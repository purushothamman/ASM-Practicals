# Practical 9: Kruskal-Wallis Test

import numpy as np
from scipy.stats import kruskal

# Sample data (3 groups / fertilizers)
M1 = np.array([7,14,14,13,12,9,6,14,12,8])
M2 = np.array([15,17,13,15,13,9,12,10,9,8])
M3 = np.array([6,8,8,9,14,14,13,8,10,9])

# Perform test
stat, p_val = kruskal(M1, M2, M3)

print("H-statistic:", stat)
print("p-value:", p_val)
