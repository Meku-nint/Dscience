# exception handling in python .
try :
    print (10 / 0) # this will raise a ZeroDivisionError
except ZeroDivisionError:
    print ("You can't divide by zero!") # this will be printed instead of the error message

finally:
    print ("This will always be executed") # this will be printed regardless of whether an exception was raised or not