#Design an algorithm that finds the maximum positive integer input by a user.
# The user repeatedly inputs numbers until a negative value is entered.


# Find the maximum positive integer of the users input.
# 1. User inputs positive integers.
# 2. When user inputs a negative value, find the maximum positive integer.


# Program starts here:

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0

# while num_int is a positive number, run while loop and then ask for new number. 
# Assign the hightest num_int to max_int.

while num_int > 0:
    if num_int > max_int:
        max_int = num_int 
    num_int = int(input("Input a number: "))

# If num_int is a negative number print...

if num_int < 0:
    print("The maximum is", max_int)    # Do not change this line

