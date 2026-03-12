# range in python is built-in function that generates a sequence of numbers.
# immutable sequence of numbers that can be used in a for loop or converted to a list.
# range(start, stop, step) where start is the starting number of the sequence, stop
# if the range function is called with only one argument,it will be the stop value and the start value will be 0 by default.

range (10)
print(range(10))
# the out put of the above code will be range(0, 10) which is a range object that represents the sequence of numbers from 0 to 9.

x=5
if x in range(10):
    print(x, "is in the range")
# if range is called in two argument form, the first argument is the start value and the second one is the stop 
x =range(1, 10)
print(x) # this will print range(1, 10) which is a range object that represents the sequence of numbers from 1 to 9.
print (list(x)) # this will print the list of the number in given range b/c it changed to list
# range can be called with three arguments, the first oen is for of the sequence, the second one is the stop value and the third one is the step value which is the difference between each number in the sequence.
x = range(1, 10, 2)
print(x) # this will print range(1, 10, 2) which is a range object that represents the sequence of numbers from 1 to 9 with a step of 2.
print(list(x)) # this will print the list of the number in given range b/c it
# the step value can be negative, which will generate a sequence of numbers in reverse order.
x = range(10, 0, -1)
print(x) # this will print range(10, 0, -1) which is
# a range object that represents the sequence of numbers from 10 to 1 with a step of -1.
print(list(x)) # this will print the list of the number in given range b/c it
# if the arguments passed are start and stop ,the stop has to be greater than step other wise the list will be empty
x = range(10, 0, 1)
print (list(x)) # the output will be empty.