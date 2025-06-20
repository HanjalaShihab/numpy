import numpy as np
#Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
arr = np.trunc([-3.1666, 3.6667])
print(arr)
print()


arr = np.fix([-3.1666, 3.6667])
print(arr)
print()


#The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
arr = np.around([3.1666, 2])
print(arr)
print()


#The floor() function rounds off decimal to nearest lower integer.
arr = np.floor([-3.1666, 3.6667])
print(arr)
print()


#The ceil() function rounds off decimal to nearest upper integer.
arr = np.ceil([-3.1666, 3.6667])
print(arr)
print()