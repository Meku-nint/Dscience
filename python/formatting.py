# string formatting in python is a way to create a new string by replacing placeholders in a template string with values.
# there are several ways to format strings in python, including:
# 1. using the % operator
# 2. using the str.format() method
# 3. using f-strings (formatted string literals)
# using the % operator
name = "Alice"
age = 30
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)
# using the str.format() method
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
# using f-strings (formatted string literals)
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

