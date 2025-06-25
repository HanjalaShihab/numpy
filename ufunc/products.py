import numpy as np

arr = np.array([1,2,3,4])
print(np.prod(arr))  #returns 1*2*3*4
print()


arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

print(np.prod([arr1, arr2]))
print()


#Product over an Axis:
print(np.prod([arr1, arr2], axis= 1)) #returns [24 1680]
print()


#Cumulative product:
arr = np.array([5,6,7,8])
print(np.cumprod(arr))