#Chi square distribution is used as a basis to varify the hypothesis
#It has two parameters:
    # df - (degree of freedom)
    # size - the shape of the returned array


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


x = np.random.chisquare(df=2, size=(2,3))
print(x)


sns.displot((np.random.chisquare(df=1, size=1000)), kind='kde')
plt.show()

