import numpy as np 

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr, 3)
print(newarr)
print()
print()



#If you split an array into 3 arrays, you can access them from the result just like any array element:
array = np.array([1,3,4,5,6,6,7,788])

new = np.array_split(array, 3)
print(new)
print()
print(new[0])
print(new[1])
print(new[2])
print()


#splitting a 2-D array:
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])

newarray = np.array_split(arr, 3)
print(newarray)