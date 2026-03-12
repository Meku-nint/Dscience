# functions in python object stored in memory and can be called by their name followed by parentheses. they can take arguments and return values.
# block of code which executes when it is called. it can be use for remove code repetition and make the code more organized and reusable.
def greet (name):
    return "Hello, " +name + "!" 
   # if the function have no return statement, it will return None by default.
greeting =greet("Alice")
print(greeting) # this will print "Hello, Alice!" which is the return value of the greet function when it is called with the argument "Alice"
def pass_statement():
    pass # this is  a placeholder for a function that does nothing,it used for creating a function that is not yet implemented or for creating a function that is used as a placeholder for a future implementation.
# parameter is a variable that is defined in the function definition and is used to receive the value passed to the function 
# argument is the actual value that is passed to the function when the function is called.
def my_function(country ="Egypt"):
    print ("I am from " + country)
my_function() # this will print "I am from Egypt" because the default value of the parameter country is "Egypt"
my_function("USA") # this will print "I am from USA" because the argument "
