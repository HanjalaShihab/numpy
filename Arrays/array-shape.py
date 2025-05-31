import numpy as np

#empty array:
arr = np.array([])
print(arr.shape)
print()

#shape of 1D array:
arr = np.array([1,2,3,5])
print(arr)
print(arr.shape)
print()


#get the shape of 2-D array:
arr_2D = np.array([[1,24,56], [6,55,87]])
print(arr_2D)
print(arr_2D.shape)
print()


#creating an array with 5 dimensions:
arr_5D = np.array([1, 2, 4, 5], ndmin= 5)
print(arr_5D)
print(arr_5D.shape)
print()