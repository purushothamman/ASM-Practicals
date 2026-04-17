import matplotlib.pyplot as plt
import numpy as np


size = 25 #No. of trials
n = 10000
p = 0.3 #Probability of sucess

np.random.seed(3)

random_binom = np.random.binomial(size,p,n)

plt.hist(random_binom,
         bins = len(np.unique(random_binom)),
         density = True)

plt.xlabel("Students Pasing In final exam")
plt.ylabel("Probability")
plt.title("Binomial Prabability Distribution \n For n = 25 and p = 0.3")
plt.xticks(range(0,size+1))
plt.show()
