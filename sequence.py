#Generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# 1. Ask user for int number for the length of the sequense.
# 2. Generate a sequense that takes the sum of the first 3 numbers in sequens to create the next number.
# 3. Only take the sum of the 3 numbers before the number to be generated to generate a new number.
# 4. Once you have generated the amount of numbers the user wanted print the sequense.


n = int(input("Enter the length of the sequence: ")) # Do not change this line

num_a = 0
num_b = 1
num_c = 0
generate_num = 0

for i in range(n):
    generate_num = num_a + num_b + num_c
    num_a = num_b
    num_b = num_c
    num_c = generate_num

    print(generate_num, end=" ")
    
    


