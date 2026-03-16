# random number is generate based on the device time or os randomness or entropy

from numpy import random
x=random.randint(10)
print(x) # this will print a random integer between 0 and 9 (inclusive)

# generate random number form array we use choice method it takes array as an argument and it will return a random element from the array
list_name=['john','michael','sarah','jessica']
random_name=random.choice(list_name)
print(random_name) # this will print a random name from the list_name array
