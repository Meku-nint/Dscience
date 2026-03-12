# built in mathematics methods
def absolute(x):
    # returns the absolute value of a number
    return abs(x)
print (absolute(-5))
def power(x, y):
    # returns the value of x raised to the power of y
    return pow(x, y)
print (power(2, 3))
def square_root(x):
    # returns the square root of a number
    return x ** 0.5
print (square_root(16))
def logarithm(x, base):
    # returns the logarithm of x to the given base
    import math
    return math.log(x, base)    
print (logarithm(100, 10))
def min_max(x, y):
    # returns the minimum and maximum of two numbers
    return min(x, y), max(x, y)     

print (min_max(5, 10))