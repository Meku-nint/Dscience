# while loop executes as long as the condition is ture.
counter = 0
while counter <5:
    print("Counter is ", counter)
    counter =counter +1
# so basically the while loop is executed till the counter is less than 5.

# break and continue statements are used to control the flow of the loop. break statement is used to exit the loop, while continue statement is used to skip the current iteration and move to the next iteration.
counter = 0
while counter <5:
    if counter == 3:
        break # this will exit the loop when counter is equal to 3
    print("Counter is ", counter)
    counter =counter +1
counter = 0
while counter <5:
    if counter == 3:
        continue # this will skip the current iteration when counter is equal to 3 and move to the next iteration
    print("Counter is ", counter)
    counter =counter +1