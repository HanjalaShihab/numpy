import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[0])

print()

print(arr[1])

print()

#adding elements of the numPy array:
print(arr[1] + arr[3])

print()


#Access 2-D arrays:
arr = np.array([[1,2,3], [4,5,6]])
print(arr)
print(arr[0, 2]) #3rd element from 1st row
print(arr[1, 1]) #2nd element from 2nd row


#
print()
print()
#


#Access 3-D array:
arr = np.array([[[4,5,6], [1,2,3]], [[54, 66, 77],[87, 35, 60]]])
print(arr)
print(arr[0, 1, 2])
print(arr[1, 0, 1])


#negative indexing:
print(arr[1, 1, -1])  #-1 will print the last value of the array
