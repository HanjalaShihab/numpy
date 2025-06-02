import numpy as np 

array = np.array([1,2,3,45])
x = np.where(array == 2)
print(x)
print()



#array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#z = array2.tolist()

#y = [x for x in z if x % 2 == 0]
#print(y)


arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.where(arr2 % 2 ==1))
print()


#using searchsorted() function, which perform a binary search in the array, 
# and return the index where the specified value would be inserted to maintain the search order

arr3 = np.array([6,7,8,9])

x = np.searchsorted(arr3, 7)
print(x)


print(np.searchsorted(arr3, 6))


#searchsorted() with multiple values:
x = []
for i in range(1, 100):
    x.append(i)
    
arr4 = np.array(x)

y = [i for i in x if i % 2 == 0]


arr5 = np.array(y)

final = np.searchsorted(arr4, arr5)
print(final, type(final))