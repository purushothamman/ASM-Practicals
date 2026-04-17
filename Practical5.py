import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom , norm


n,p = 13,0.7
x = np.arange(0,n+1)

print("PmF (x=6)",binom.pmf(6,n,p))

print("cmf (x<=9) : ",binom.cdf(6,n,p))

plt.plot(x,binom.pmf(x,n,p))
plt.title("Binomial PMF")
plt.show()

plt.step(x,binom.cdf(x,n,p))
plt.title("Binomial cdf")
plt.show()


#PDf and CDF in normal

x = np.linspace(-4,4,100)

plt.plot(x,norm.pdf(x))
plt.title("Normal PMF")
plt.show()

plt.plot(x,norm.cdf(x))
plt.title("Normal CMF")
plt.show()


mu , sigma = -4 , np.sqrt(3)
data = np.random.normal(mu,sigma,500)

plt.hist(data,density = True)
plt.plot(x,norm.pdf(x,mu,sigma))
plt.title("Histogram with PDF")
plt.show()

