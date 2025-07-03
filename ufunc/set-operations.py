#A set in mathematics is a collection of unique elements:
#Set are used for operations involving frequent intersection, union and difference operations.

import numpy as np

arr = np.array([1,1,1,2,3,4,5,5,6,7])

x = np.unique(arr)  #it will remove the duplicate values
print(x)


#Finding union:
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
