#NumPy provides the ufuncs sing(), cos(), tan() that take values in radians and produce the corresponding values.

import numpy as np

x = np.sin(np.pi/2)
print(x)
print()


#Find sine values for all the values in arr:

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)
print(x)
print()


#Convert degrees into radians:
arr = np.array([90,180, 270, 360])
x = np.deg2rad(arr)
print(x)