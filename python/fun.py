print ("welcome to python")
# in programming there is a concept translation which is the process of converting high level language to low level language
# python is a high level language and it is interpreted language which means that it is not compiled to machine code before execution but rather it is executed line by line by an interpreter
# syntax is the set of rules that defines the structure of the code and how it should be written
# semantics is the meaning of the code and how it is executed
# variables are used to store data and they can be of different types such as int, float, str, bool, list, tuple, set, dict
# statements are the instructions that are executed by the interpreter and they can be simple or compound statements
userINput =input ("enter your name: ")
x=int(userINput)
if x>2:
    print (x, "is greater than two")
elif x==2:
    print (x, "is equal to two")
else :
    print (x, "is not greater than two")

# for multi line comments we can use triple quotes
"""
this is a multi line comment
it can be used to explain the code in detail
or to provide documentation for the code
"""
# the types of data in python are int, float, str, bool, list, tuple, set, dict
x =12
print (type(x))
y = 3.14
print (type(y))
z = "hello"
print (type(z))
# multi word variable names can be created using d/t rule 
# camelCase: myVariableName like the first letter of each word is capitalized except the first word
# snake_case: my_variable_name like all letters are lowercase and words are separated by underscores
myVariableName = "camelCase"
my_variable_name = "snake_case"
# pascal case: MyVariableName like the first letter of each word is capitalized
MyVariableName = "pascalCase"
# data types in python 
