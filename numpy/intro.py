# numpy (numeric python) is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.
# numpy is 50x faster than regular python lists b/c it is implemented in C and uses optimized algorithms for array operations. it also provides a convenient way to perform element-wise operations on arrays, which can be much faster than using loops in python.
# b/c numpy store the data in a contiguous block of memory, it can take advantage of cache locality, which can further improve performance. numpy also provides support for broadcasting, which allows you to perform operations on arrays of different shapes and sizes without the need for explicit loops.
# np is a common alias for numpy.
import numpy as np
# zero dimensional array (scalar)
zero_dim_array=np.array(42)
print(zero_dim_array) 
print(zero_dim_array.ndim) 