# onrmal distribution is a continuous probability distribution that is defined by a bell-shaped curve. it is also known as the Gaussian distribution. the normal distribution is defined by two parameters: the mean (mu) and the standard deviation (sigma). the mean is the center of the distribution and the standard deviation is a measure of how spread out the distribution is. the normal distribution is used to model many natural phenomena such as heights, weights, test scores, etc.
from numpy import random

# it has three parameter loc - mean,scale -sd and size the shape of the returned array.
x=random.normal(loc=1.0, scale=2.0, size=(2,3))
print(x) 