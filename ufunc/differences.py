# Discrete difference(which means subtracting two successive elements)
import numpy as np

x = np.array([1,2,3,4,5])
print(np.diff(x))  # [2-1, 3-2, 4-3, 5-4]
print()


#we can perform this difference repeatedly by giving 'n' parameter:
array = np.array([4,7,10,7])
print(np.diff(array, n=2))