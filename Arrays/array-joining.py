import numpy as np 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

array = np.concatenate((arr1, arr2))
print(array)
print()
print()


#Joining two 2-D array along rows(axis = 1):
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[6,7],[8,9]])

array2 = np.concatenate((arr1, arr2), axis=1) #it will concatenate column by column
#if no axis is given, the default is 0
print(array2)  
print()
print()


#joining arrays using stack()  functions:
arr1 = np.array([1,2,3])
arr2 = np.array([5,6,7])

array = np.stack((arr1, arr2), axis=1)  #it makes the row into column
print(array)
print()


array2 = np.hstack((arr1, arr2))   #same as concatenation
print(array2)
print()


array3 = np.vstack((arr1, arr2))
print(array3)
print()


#joining along heigh:(same as only stack() function)
array4 = np.dstack((arr1, arr2))
print(array4)