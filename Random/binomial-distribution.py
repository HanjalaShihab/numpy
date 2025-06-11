from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.binomial(n= 10, p = 0.5, size=500)
print(x)
print()


#sns.displot(x)
#plt.show()


#we can show normal and binomial distributions together in a single diagram-

data = {
    "normal": random.normal(loc=35, scale= 5, size= 500),
    "binomial": random.binomial(n = 70, p = 0.5, size=500)
}

sns.displot(data, kind="kde")
plt.show()