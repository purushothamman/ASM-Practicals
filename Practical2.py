import pandas as pd
import numpy as np
from scipy.stats import norm

# Create sample dataset
data = {
    'gender': ['Male','Male','Female','Male','Female','Male','Male','Female'],
    'height': [170, 168, 160, 175, 158, 172, 169, 162]
}

students = pd.DataFrame(data)

# Filter males
males = students[students['gender'] == 'Male']

# Mean & SD
height_mean = males['height'].mean()
height_sd = males['height'].std()

print("Mean:", height_mean)
print("SD:", height_sd)

# Probability for 168
x = 168
x_z = (x - height_mean) / height_sd
print("P(X ≤ 168):", norm.cdf(x_z))

# Probability for 175
x1 = 175
x1_z = (x1 - height_mean) / height_sd
print("P(X ≤ 175):", norm.cdf(x1_z))

print(males)