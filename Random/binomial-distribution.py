#Binomial Distribution is a Discrete Distribution.

#It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
#It has three parameters:
    #n - number of trials.
    #p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
    #size - The shape of the returned array.

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