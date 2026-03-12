# dictionary in python is a collection of key-value pairs. it is unordered, changeable, and does not allow duplicate keys.
personInfo={
       "name": "john",
       "age":23,
       "city":"new york"
}
print (type(personInfo)) # this will print <class 'dict'> which indicates that personInfo is a dictionary data type
print(personInfo["name"]) # this will print "john" which is the value associated with the key "name"
for x in personInfo:
    print (personInfo[x]) # this will print the values in the dictionary which are "john", 23, and "new york"