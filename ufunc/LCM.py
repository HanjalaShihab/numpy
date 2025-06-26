#LCM = Longest Common Multiple
#LCM (Lowest Common Multiple) of two or more numbers is the smallest number that is a multiple of each of those numbers.

#For example, multiples of 4 are 4, 8, 12, 16, 20, ...
              #Multiples of 6 are 6, 12, 18, 24, 30, ...
#The lowest common multiple of 4 and 6 is the smallest number that appears in both lists of multiples. Here, it is 12.

import numpy as np

x = 4
y = 6

z = np.lcm(x,y)
print(z)


#if I want to find out LCM of a array:
arr = np.array([2,6,9])
print(np.lcm.reduce(arr))


#arranging arrays:
arr = np.arange(1,11)
print(np.lcm.reduce(arr))


array = np.array([4,5,6,7,8])
y = np.lcm.reduce(array)

print(y)