# shape of an array is the number of elements in each dimension of the array. it is represented as a tuple of integers. the length of the tuple is the number of dimensions of the array. for example, a 2D array with 3 rows and 4 columns will have a shape of (3,4). a 3D array with 2 matrices, each with 3 rows and 4 columns will have a shape of (2,3,4).
# numpy array has an attribute called shape that returns the shape of the array as a tuple of integers. you can also use the reshape() method to change the shape of an array without changing its data. for example, if you have a 1D array with 12 elements, you can reshape it into a 2D array with 3 rows and 4 columns using the reshape() method.
import numpy as np
# create a 1D array with 12 elements
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.shape) # this will print (12,) which means it is a 1D
# reshape the 1D array into a 2D array with 3 rows and 4 columns
reshaped_arr=arr.reshape(2,4)
print(reshaped_arr)
print(reshaped_arr.shape) # this will print (3,4) which means it