# view is a way to create a new array with share memory ,and data the original array.

import numpy as np
original =np.array([1,2,3,4,5])
view_array=original.view() # this will create a new array that shares the same data as the original array. so any changes made to the view_array will also affect the original array.
# copy is a way to create a new array with its own data, and it does not share memory with the original array.
copy_array=original.copy() # this will create a new array that has its own data, and it does not share memory with the original array. so any changes made to the copy_array will not affect the original array.
original[0]=20
print(original) # since the original array has been modified, it will print [20,2,3,4,5]
print(view_array) # since the view_array shares the same data as the original array, it will also reflect the change made to the original array. so it will print [20,2,3,4,5]
print(copy_array) # since the copy_array has its own data, it will not reflect the change made to the original array. so it will print [10,2,3,4,5]