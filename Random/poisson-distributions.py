#Poisson Distribution is a Discrete Distribution.

#It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?
    #It has two parameters:
    # lam - rate or known number of occurrences e.g. 2 for above problem.
    # size - The shape of the returned array.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.poisson(lam = 2, size = 10)
print(x)


sns.displot(x, kind='kde')
plt.show()