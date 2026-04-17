import numpy as np
from scipy.stats import binomtest
from statsmodels.sandbox.stats.runs import runstest_1samp

# Sign Test
before = np.array([20,22,19,24,21])
after  = np.array([23,25,20,26,22])

diff = after - before
p = binomtest(sum(diff>0), len(diff), 0.5).pvalue
print(p)

# Run Test
data = np.array([1,2,3,2,1,2,3])
print(runstest_1samp(data)[1])