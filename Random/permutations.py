from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])

random.shuffle(arr)  #shuffle() method makes changes to the original array
print(arr)
print()



#to make a re-arranged array by leaving the original array unchanged:
arr = np.array([5,6,7,8,9])
print(random.permutation(arr))
print()



#2-D array permutation:
array = np.array([[1,2,3,4,5],[6,7,8,8,9]])
print(random.permutation(array.flatten()).reshape(array.shape))