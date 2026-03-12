# functions in python object stored in memory and can be called by their name followed by parentheses. they can take arguments and return values.
# block of code which executes when it is called. it can be use for remove code repetition and make the code more organized and reusable.
def greet (name):
    return "Hello, " +name + "!" 

greeting =greet("Alice")
print(greeting) # this will print "Hello, Alice!" which is the return value of the greet function when it is called with the argument "Alice"