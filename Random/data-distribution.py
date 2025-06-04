#Data Distribution is a list of all possible values, and how often each value occurs.
#The choice() method allows us to specify the probability for each value.


from numpy import random

arr = random.choice([4,5,7,9], p=[0.2, 0.3,0.5,0.0], size=(10))
print(arr)



#
print()
print()
#


array = random.choice([1,2,3,4], p=(0.6,0.2,0.1,0.1), size=(3,2))
print(array)