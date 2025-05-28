import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print()


print(arr[4: ])
print()


print(arr[:4])
print()


print(arr[-3: -1])
print()


#using STEP parameter or value to determine the step of the slicing:
print(arr[1:5:2])
print()


print(arr[::2])
print()


arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr[1, 1:3])
print(arr[0, :3])
print(arr[0:2,2])