# Lesson 08_Arithmetic Operations with Numbers in Python
# Practicing
# Date: 2025-07-05

print( 6 + 2 )  # Adds 6 and 2, outputs 8
print( 6 - 2 )  # Subtracts 2 from 6, outputs 4
print( 6 * 2 )  # Multiplies 6 by 2, outputs 12
print( 6 / 2 )  # Divides 6 by 2, outputs 3.0
print( 7 // 2 ) # Integer division of 7 by 2, output 3
print( 6**2)    # Raises 6 to the power of 2, output 36
print( 7 % 2)   # Gets reminder of 7 divided by 2, outputs 1

number = 3 + 4 * 5**2 + 7
print(number)   # Outputs 110; Calculation steps: 5^2=25 > 4*25=100 > 3+100=103 > 103+7=110

number = (3 + 4) * (5**2 + 7)
print(number)   # Calculation steps: (3 + 4)=7 > (5^2 + 7) = (25 + 7) = 32 > 7 * 32 = 224

number = 10 # Set a variable to 10
number += 5 # Add 5 to number, same as number = number + 5
print(number)   # Outputs 15
number -= 3 #Subtract 3 from number, same as number = number - 3
print(number)   # Outputs 12
number *= 4   # Multiply number by 4, same as number = number * 4
print(number)   # Output 48

x = 10  # Set x to 10
x += 5  # Add 5 to x
print(x)    # Outputs 15

x = 3   # Set x to 3
x += 2  # Add 2 to x
print(x)    # Outputs 5

x = 5 # Set x to 5
x -= 2  # Subtract 2 from x
print(x)    # Outputs 3

x = 4   # Set x to 4
x *= 3  # Multiply x by 3
print(x)    # Outputs 12

x = 8    # Set x to 8
x /= 2    # Divide x by 2
print(x)    # Outputs 4.0

x = 9   # Set x to 9
x //= 2    # Integer divide x by 2
print(x)    # Output 4

x = 2   # Set x to 2
x **= 3    # Raise x to the power of 3
print(x)    # Outputs 8

x = 10 # Set x to 10
x %= 3    # Take remainder of x divided by 3
print(x)    # Outputs 1

# Practicing

x = 5   # Set x to 5
x += 10    # Add 10 to x
print(x)    # Outputs 15

y = 20  # Set y to 20
y /= 4    # Divide y by 4
print(y)    # Outputs 5.0

z = 7   # Set 7 to z
z **= 2    # Square z
print(z)    # Outputs 49
