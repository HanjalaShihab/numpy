#Used to describe probability where every event has equal chances of occuring.
#E.g. Generation of random numbers.

#It has three parameters:
    #low - lower bound - default 0 .0.
    #high - upper bound - default 1.0.
    #size - The shape of the returned array.


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


x = np.random.uniform(size=(1000))
print(x)


sns.displot(x, kind='kde')
plt.show()