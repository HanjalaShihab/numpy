import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = np.reshape(arr, (2, 3, 2))
print(newarr)
print()
print()
print()



# or we could do this instead:
againnewarr = arr.reshape(2,3,2)
print(againnewarr)
print()
print()
print()



agnarr = np.reshape(arr, (4, 3))
print(agnarr)
print()
print()



#we can check the base if it is a copy or view of the original array:
print(agnarr.base)  #so its a view as it returns the original array
print()
print()



#converting a 2-D array into 1-D:
arr = np.array([[1,2,3,4], [5,6,7,8]])
newarr = np.reshape(arr, (-1)) #we could also use '6' instead of '-1' as it represents 1-D array

print(newarr)