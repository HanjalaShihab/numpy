# lLogistic Distribution is used to describe growth.

#Used extensively in machine learning in logistic regression, neural networks etc.

#It has three parameters:
    #loc - mean, where the peak is. Default 0.
    #scale - standard deviation, the flatness of distribution. Default 1.
    #size - The shape of the returned array.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


x = np.random.logistic(loc=1, scale=2, size=1000)
print(x)
print()


sns.displot(x, kind='kde')
plt.show()



data = {
    "normal": np.random.normal(scale=2, size=1000),
    "logistic": np.random.logistic(size=(1000))
}

sns.displot(data, kind='kde')
plt.show()