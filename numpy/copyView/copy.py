# view is a way to create a new array with share memory ,and data the original array.

import numpy as np
original =np.array([1,2,3,4,5])
view_array=original.view() # this will create a new array that shares the same data as the original array. so any changes made to the view_array will also affect the original array.
original[0]=10
print(view_array) # since the view_array shares the same data as the original array, it will reflect the change made to the original array. so it will print [10,2,3,4,5]