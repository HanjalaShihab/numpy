import numpy as np

# Addition:
arr1 = np.array([10,20,30,40,60])
arr2 = np.array([70,80,90,30,43])

addition = np.add(arr1, arr2)
print(addition)
print()


# Substraction:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

substraction = np.subtract(arr1, arr2)
print(substraction)
print()


# Multiplication:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

multiplication = np.multiply(arr1, arr2)
print(multiplication)
print()


# Division:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

division = np.divide(arr1, arr2)
print(division)
print()


# Power:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 2, 2, 3, 4, 5])

power = np.power(arr1, arr2)
print(power)
print()


# Mod and Remainder:
   # we can use the mod() and remainder() methods for this


# Quotient and Mod:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)    #divmod() function returns both quotient and the mod
print(newarr)
print()


# Absolute values:
arr = np.array([-1, -2, 1,2, 3, -4])

absolute = np.absolute(arr)
print(absolute)
print()