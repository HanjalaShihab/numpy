import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

filter_arr = []

for i in arr:
    if i % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)


newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print()


#or we could use the shorthand for this-
filter_new = arr % 2 == 1
newarray = arr[filter_new]
print(filter_new)
print(newarray)
print()



arr = np.array([40, 10, 50, 20, 44, 63, 26])

filter_arr = arr > 30

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print()

