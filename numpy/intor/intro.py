# numpy (numeric python) is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.
# numpy is 50x faster than regular python lists b/c it is implemented in C and uses optimized algorithms for array operations. it also provides a convenient way to perform element-wise operations on arrays, which can be much faster than using loops in python.
# b/c numpy store the data in a contiguous block of memory, it can take advantage of cache locality, which can further improve performance. numpy also provides support for broadcasting, which allows you to perform operations on arrays of different shapes and sizes without the need for explicit loops.
# np is a common alias for numpy.
import numpy as np
# zero dimensional array (scalar)
zero_dim_array=np.array(42)
print(zero_dim_array) 
print(zero_dim_array.ndim) 

# one dimensional array (vector)
one_dim_array=np.array([1,2,3,4,5])
print(one_dim_array)
print(one_dim_array.ndim)

# two dimensional array (matrix) an array with two axes (rows and columns). it is represented as a list of lists in python. each inner list represents a row of the matrix.
two_dim_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_dim_array)
print(two_dim_array.ndim)

# three dimensional array (tensor) an array with three axes. it is represented as a list of lists of lists in python. each inner list represents a 2D matrix.
three_dim_array=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
print(three_dim_array)
print(three_dim_array.ndim)
print(three_dim_array[0,1,2]) # this means the first 2D matrix, second row, third column (0-based indexing)
# 0 indicates the first 2D matrix, 1 indicates the second row, and 2 indicates the third column. so it will return the value 6.(so ,2Dmatrix,row,column)