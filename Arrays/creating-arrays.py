#NumPY is used to work with arrays. The array object in NumPy is called ndarray.

import numpy as np

arr = np.array([1, 2, 4, 5 ,6,7])
print(arr)


#
print()
#


#Dimensions in arrays

# 0-D array:
arr1 = np.array(42)
print(arr1)


#
print()
#


# 1-D array:
arr2 = np.array([1, 2, 3, 5,8])
print(arr2)


#
print()
#


#2-D array:
arr3 = np.array([[5,6,7], [8, 9 , 10]])
print(arr3)


#
print()
print()
#


#3-D array:(an array that has 2-D arrays(matrices) as its elements is called 3-D array)
   #creating a 3-D array with two 2-D arrays
arr4 = np.array([[[1,2,3], [4,5,6]],[[7,8,9], [10, 11, 12]]])
print(arr4)


#
print()
print()
#


#checking the number of dimensions used in the numpy arrays:
print(arr1.ndim, "dimension")
print(arr2.ndim, "dimension")
print(arr3.ndim, "dimension")
print(arr4.ndim, "dimension")