#TO create a ufunc we should define a normal function first.then add the function to NumPy ufunc
    # with the frompyfunc() method

# frompyfunc() method takes three arguments:
         # function - the name of the function
         # inputs - the number of the input arguments(arrays)
         # output - the number of output arrays

         # like -  np.frompyfunc(myfunc, nin, nout)

import numpy as np

def myfunction(x, y):
    return x + y

myfunction = np.frompyfunc(myfunction, 2, 1)
print(myfunction([1,2,3,4],[5,6,7,8]))