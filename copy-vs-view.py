#The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

#The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

#The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.


#making a copy of an exiting array:
import numpy as np

arr = np.array([1,2,3,4])

x = arr.copy().astype(float)   #astype() function is optionally used here.
print(arr)
print(x)
print(x.dtype)
print()

#making a view of an exiting arrya:
arr = np.array([3,4,5,6])

y = arr.view()
print(arr)
print(y)
print()


#changing the original arrays elements to see if the copy array changes:
array = np.array([40, 2,3,4])
m = array.copy()
array[0] = 1

print(array)
print(m)
print()


#changing the original arrays elements to see if the view array changes:
arr = np.array([50, 2,3,4])
r = arr.view()
arr[0] = 1

print(arr)
print(r)
print()


#changing the view array elements:
r[0] = 100
print(r)
print(arr)
print()


  #or
r[0 : 2] = [89,95]  #using array slicing
print(r)
print(arr)
print()



#check if Array owns its Data:(using the base attribute)
arr = np.array([1, 2, 3, 4, 5])

x= arr.copy()
y= arr.view()


print(x.base)
print(y.base)