# slicing in python means taking elements from one given index to another given index.

# in slicing [1:5] the result include the lower bound but exclude the upper bound.

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
arr2=arr[1:5] # this will return a new array that contains the elements from index 1 to index 4. so it will return [2,3,4,5]
print(arr2)
# negative slicing 
print(arr[-5:-1]) # this will return a new array that contains the elements from index -5 to index -2. so it will return [5,6,7,8] till the upper bound not included
