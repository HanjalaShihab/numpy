import numpy as np


#1-D array:
arr = np.array([1,2,3,4])

for x in arr:
    print(x)
    
    

print()
print()



#2-D array:
arr = np.array([[1,2,4], [6,7,8]])

for x in arr:
    for y in x:
        print(y)
        
        
print()
print()



#3-D array:
arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)
            
            
print()
print()



#but we can't iterate with for loop all the time, like if there is a high demnsioned array!
# so we can use nditerator() funciton here to iterate:
array = np.array([[[1,2,3],[5,6,7]],[[9,10,11],[13,14,15]]])

for x in np.nditer(array):
    print(x)
    

print()
print()



#we can convert the array type also in nditer function:
arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

for x in np.nditer(arr, flags=["buffered"], op_dtypes=['S']):
    print(x)
    

print()
print()


#we use  ndenumerate() function to print the values with index numbers:
arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

for i,x in np.ndenumerate(arr):
    print(i, x)