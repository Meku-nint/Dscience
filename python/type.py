# list is data type in python that is used to store multiple items in a single variable.
# lists are ordered, changeable, and allow duplicate values.
mylist = ["zapple", "banana", "cherry"]
print (type(mylist)) # this will print <class 'list'> which indicates that mylist is a list data type
print (mylist[0]) # this will print the first item in the list which is "zapple"
# lists are mutable and allow duplicate values
mylist[0] = "apple" # this will change the first item in the list
len(mylist) # this will return the number of items in the list which is 3
# len() is a built-in function in python that returns the number of items in an object.
mylist.append("orange") # this will add "orange" to the end of the list
# .append() is a method that adds an item to the end of the list. we call it method because it is a function that is associated with an object which in this case is the list.
# list can contain different data types
myList= ["apple", 1, 3.14, True]
# check an item in a list
newList= ["apple", "banana", "cherry"]
if "banana" in newList:
    print ("yes, banana is in the list")
else :
    print ("no, banana is not in the list")
    