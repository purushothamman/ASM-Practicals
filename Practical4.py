# Practical 4 without dataset

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Create sample height data
female_heights = np.array([150, 155, 160, 162, 158, 165, 170, 168, 172, 159])

# Mean and Standard Deviation
mean = np.mean(female_heights)
sd = np.std(female_heights, ddof=1)

print("Mean:", mean)
print("SD:", sd)

# Histogram
plt.hist(female_heights, density=True)

# Normal curve
x = np.linspace(140, 190, 100)
y = norm.pdf(x, mean, sd)

plt.plot(x, y)

plt.title("Normal Distribution (Female Height)")
plt.xlabel("Height")
plt.ylabel("Density")
plt.show()
    
