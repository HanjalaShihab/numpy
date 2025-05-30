#By default python have these data types:
    #strings
    #integer
    #float
    #boolean
    #complex
    

#Data types in NumPy:
     # i - integer
     # b - boolean
     # u - unsigned integer
     # f - float
     # c - complex float
     # m - timedelta
     # M - datetime
     # O - object
     # S - string
     # U - unicode string
     # V - fixed chunk of memory for other type (void)
     

#Checking the data type of an array object:
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)   
print()



arr = np.array(["apple", "banana", "cherry"])
print(arr.dtype)
print()
  


#creating arrays with a defined data type:
arr = np.array([1, 2, 3, 4, 5], dtype= 'S')
print(arr)
print(arr.dtype)
print()



# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method:
    # astype() function creates a copy of the array, and allow to specify the data type as a parameter

arr = np.array([1.1, 2.1, 3.4])

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
print()



arr = np.array([1,2,3,4,8,10])

newarray = arr.astype('f')
print(newarray)
print(newarray.dtype)
print()


new = arr.astype('c')
print(new)
print(new.dtype)
print()


# or we could directly put the type in astype() function:
arr = np.array([1.5, 5.5, 6.3, 9.9])

new = arr.astype(int)

print(new)
print(new.dtype)
print()