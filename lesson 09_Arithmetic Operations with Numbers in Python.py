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