# Lesson 13_Binary Representation of Numbers in Python
# Practicing
# Date: 2025-07-08

number = 0b101  # define a number using binary (0b101 = 5)
print(f"number = {number:0b}")  # print the number in binary format (prints 101)
print(f"number = {number}") # print the number in decimal format (prints 5)

# Practicing

number_1 = 0b111    # define number_1 with a binary value (0b111 is 7 in decimal)

print(f"number_1 = {number_1:0b}")  # print number_1 in binary format (will display '111')

print(f"number_1 = {number_1}") # print number_1 in decimal format (will display '7')

number_2 = 0b1001   # define number_2 with a binary value (0b1001 is 9 in decimal)

print(f"number_2 = {number_2:0b}")  # print number_2 in binary format (will display '1001')

print(f"number_2 = {number_2}") # print number_2 in decimal format (will display '9')

print(f"x = {number_1} + {number_2}")   # print the addition expression in decimal format before calculation (will display 'x = 7 + 9')

a = number_1 + number_2 # calculate the sum of number_1 and number_2, store in 'a' (will be 16)

print(f"x = {a}")   # print the result of the sun in decimal format (will display 'x = 16')

print(f"number_1 = {number_1}; number_2 = {number_2}; x = {a:0b}")  # print all values in binary format (will display 'number_1 = 111'; number_2 = 1001; x = 10000')
