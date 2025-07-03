import numpy as np

gcd = np.gcd(2, 6)
print(gcd)


arr = np.array([1,2,3,4,5,6])

x = np.gcd.reduce(arr)
print(x)