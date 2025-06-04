from numpy import random

x = random.randint(100)  #will print any random from 0 to 100
print(x)
print()


#random int with declaration of size(how many):
m = random.randint(10, size = (4))
print(m)
print()


#to get a random float number:
y = random.rand()  #it will print a random float from 0 to 1
print(y)
print()


#to specify how many random float needed:
z = random.rand(10)
print(z)
print()


#creating 2-D array of rows and columns of random floats:
n = random.rand(3, 3)
print()


#to create a 2-D array with multiple rows and columns:
a = random.randint(10, size= (2,3))
print(a)
print()


#got an array from which WE HAVE TO MAKE ARRAYS WITH RANDOM SIZES:
final = random.choice([1,2,3,4,5,6,7], size=(2,3))