# data distribution is a way to describe how the data is distributed. it can be used to model the data and make predictions about the data. numpy has a lot of built-in functions to generate random numbers from different distributions. these functions are available in the numpy.random module. you can use these functions to generate random numbers from different distributions such as normal, uniform, binomial, etc.
# probability density function (pdf) is a function that describes the probability of a random variable taking on a particular value. it is used to model the distribution of a random variable. the pdf is defined as the derivative of the cumulative distribution function (cdf). the cdf is defined as the integral of the pdf. the pdf can be used to calculate the probability of a random variable taking on a particular value by integrating the pdf over a range of values.
# choice method is a method that is used to generate random numbers from a given array. it takes an array as an argument and returns a random element from the array. it can be used to generate random numbers from a given set of values. it can also be used to generate random numbers from a given set of probabilities. it can be used to generate random numbers from a given set of weights. it can be used to generate random numbers from a given set of probabilities and weights.
from numpy import random

x=random.choice([3,4,5,6,7,8,9], p=[0.9,0.0,0.0,0.0,0.0,0.05,0.05])

print(x)
# so this one most of the time the result will be 3 b/c the probability of 3 is 0.9 and the probability of other numbers is 0.0 or 0.05. so the result will be 3 most of the time and sometimes it will be 8 or 9.

# random permutations is an arrangement of elements.
# shuffle method is a method that is used to generate random permutations of a given array.
arr = [1, 2, 3, 4, 5]
random.shuffle(arr)
print(arr) # this will print a random permutation of the array arr. the output will be different every time you run the code.

# permutation () method returns a re-arranged array and leaves the original array as un-changed.
arr = [1, 2, 3, 4, 5]
permuted_arr = random.permutation(arr)
print(permuted_arr)
print("original array" ,arr)