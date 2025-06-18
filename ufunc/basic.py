# ufunc stands for universal functions and they are NumPy functions that operate on the ndarray object.
#ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
  
   #Converting iterative statements into a vector based operation is called vectorization.
   #It is faster as modern CPUs are optimized for such operations.


# without ufunc:
x = [1,2,3,4]
y = [6,7,8,9]
z = []

for i, j in zip(x,y):
    z.append(i + j)

print(z, type(z))
print()


# but with ufunc:
import numpy as np
print(np.add(x,y), type(np.add))
print()