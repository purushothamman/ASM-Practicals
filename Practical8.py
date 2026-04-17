import numpy as np
from scipy.stats import binomtest
from statsmodels.sandbox.stats.runs import runstest_1samp

# -------------------------------
# 1. Sign Test (Paired Data)
# -------------------------------

# Sample data (before & after)
before = np.array([20, 22, 19, 24, 21])
after  = np.array([23, 25, 20, 26, 22])

# Differences
diff = after - before

# Count positives
pos = np.sum(diff > 0)
n = len(diff)

# Perform sign test
p_val = binomtest(pos, n, 0.5)

print("Sign Test p-value:", p_val)


# -------------------------------
# 2. Run Test
# -------------------------------

# Sample data
data = np.array([1, 2, 3, 2, 1, 2, 3, 2, 1])

z_stat, p_val = runstest_1samp(data)

print("Run Test p-value:", p_val)
