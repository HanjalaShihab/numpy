#A set in mathematics is a collection of unique elements:
#Set are used for operations involving frequent intersection, union and difference operations.

import numpy as np

arr = np.array([1,1,1,2,3,4,5,5,6,7])

x = np.unique(arr)  #it will remove the duplicate values
print(x)
print()


#Finding union:
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])

newarr = np.union1d(arr1,arr2)
print(newarr)


#Finding intersection:
x = np.intersect1d(arr1, arr2, assume_unique=True)  #it will find the common elements
print(x)


#Finding difference:
y = np.setdiff1d(arr1, arr2, assume_unique=True)
print(y)


#Symmetric difference(deleting only commons):
y = np.setxor1d(arr1, arr2, assume_unique=True)
print(x)