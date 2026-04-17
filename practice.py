import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


Data = {
    'gender': ['male','female','male','female','male','female','male','female'],
    'height': [170, 160, 168, 158, 175, 165, 172, 162]
}
df = pd.DataFrame(Data)

female = df[df['gender']=='female']
female =female.drop(columns=['gender'])
print(female)


#MEan and SD

mean = female['height'].mean()
sd = female['height'].std()
print("Mean:", mean)
print("SD:", sd)

#Hist 

plt.hist(female, density=True)

x = np.linspace(140,190,100)
y = norm.pdf(x,mean,sd)
plt.plot(x,y)
plt.title("Normal Distribution (Female Height)")
plt.xlabel("Height")
plt.ylabel("Density")
plt.show()