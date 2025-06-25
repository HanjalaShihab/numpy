# Addition is done between two arguments, where summation happens over n elements.

import numpy as np

arr1= np.array([1,2,3])
arr2= np.array([1,2,3])

print(np.sum([arr1, arr2]))  #returns 12
print()



#sum over an Axis:
    #if axis = 1 is specified, NumPy will sum the numbers in each array:

newarr = np.sum([arr1, arr2], axis=1)
print(newarr)  #return [6,6]
print()


# cumulative sum(partially adding the elements in array):
arr = np.array([1,2,3])
newarray = np.cumsum(arr)   #returns [1  3  6]  (1, 1+2, 1+2+3)