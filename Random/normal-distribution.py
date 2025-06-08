#Use the random.normal() method to get a Normal Data Distribution.

#It has three parameters:
   #loc - (Mean) where the peak of the bell exists.
   #scale - (Standard Deviation) how flat the graph distribution should be.(the difference between each number in the x-axis)
   #size - The shape of the returned array.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

arr = np.random.normal(loc= 1, scale= 2, size=(2,3))

arrFinal = arr.flatten()
print(arr)



#
#
#
x = np.random.normal(loc= 10, scale= 5, size=(500))

sns.displot(x, kind='kde')
plt.show()