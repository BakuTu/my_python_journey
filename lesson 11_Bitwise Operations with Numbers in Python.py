# Lesson 11_Bitwise operations with Numbers in Python
# Practicing
# Date: 2025-07-06

x = 5   # set x to 5 (0b0101 in binary)
y = 3   # set y to 3 (0b0011 in binary)

print(x & y)    # AND: gives 1 (only the last bit is 1)

print(x | y)    # OR: gives 7 (all bits where at least one is 1)

print(x ^ y)    # XOR: gives 6 (bits are different)

print(~x)   # NOT: gives -6 (inverts bits)

print(x << 1)   # Shift left: gives 10 (multiplies by 2)

print(x >> 1)   # Shift right: gives 2 (divides by 2)

# Practicing

a = 6
b = 4

print(a & b)

print(a | b)

print(a ^ b)

x = 3
print(x << 2)

c = 2
print( ~ c )

# Material

print(5 & 3)    # 1 -> AND
# 5: 0101
# 3: 0011
# Result 0001 -> 1 : COMPARES EACH BEAT OF TWO NUMBERS AND RETURNS 1 IF BOTH BITS ARE 1

print(5 | 3)    # 7 -> OR
# 5: 0101
# 3: 0011
# Result 0111 -> 7 : COMPARES EACH BIT OF TWO NUMBERS AND RETURNS 1 IF AT LEAST ONE BIT IS 1

print(5 ^ 3)    # 6 -> XOR
# 5: 0101
# 3: 0011
# Result 0110 -> 6 : RETURNS 1 IF BITS ARE DIFFERENT, OTHERWISE 0

print(~5)   # -6 -> NOT
# 5: 00000101
# ~5: 11111010 : INVERTS ALL THE BITS OF A NUMBER

print(5 << 1)   # 10 : << SHIFT LEFT
# 5: 0101
# << 1: 1010 -> 10 : SHIFTS THE BITS OF A NUMBER TO THE LEFT, ADDING ZEROS ON THE RIGHT. IT MULTIPLIES BY 2 by THE POWER OF THE SHIFT.

print(5 >> 1) # 2 : >> SHIFT RIGHT
# 5: 0101
# >> 1: 0010 -> 2 : SHIFT THE BITS OF A NUMBER TO THE RIGHT, REMOVING SHIFTED BITS. IT DIVIDES BY 2 TO THE POWER OF THE SHIFT.

# Practicing

# If there are 4 lights: 1010 and 1100, find the result using `&`
a = 0b1010
b = 0b1100
print(a & b)    # 1000 -> 0b1000 in decimal = 8

# What will happen with `|` for 1010 and 0101?
a = 0b1010  # 10 in decimal
b = 0b0101  # 5 in decimal
print(a | b)    # 0b1111 -> 15 in decimal

# Shift 0001 to the left by 2 (`<< 2`)
x = 0b0001
print(bin(x << 2))

# Print the result of `4 << 2` (think how many times the number will increase).
print(bin(4 << 2))  # 0b10000
print(4 << 2)   # 16

print(bin(16 >> 3))
print(16 >> 3)  #2










