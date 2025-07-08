# Lesson 12_ Special Topic: Bitwise operations in Python
# Practicing
# Date: 2025-07-07

# Bitwise AND
a = 0b1100  # 12
b = 0b1010  # 10
print(bin(a & b))   # ob1000 -> 8
print(a & b)

# Bitwise OR
print(bin(a | b))   # 0b1110 -> 14
print(a | b)

# BITWISE XOR
print(bin(a ^ b))   # 0b0110 -> 6
print(a ^ b)

# BITWISE NOT
print(bin(~a))  # -13 (two's complement representation)
print(~a)

# Left shift
print(bin(a << 2))  # 0b110000
print(a << 2)

# Right shift
print(bin(a >> 2))  # 0b11 -> 3
print(a >> 2)

a = 12
print(~ a)   # -13
print(bin(~ a)) # -0b1101

print(~ 5)
print(bin(~ 5))

b = 0
print(~ b)
print(bin(~ b))

print(bin(~ 0b1010))
print(~ 0b1010)

n = 0b1010
bits = 4
mask = (1 << bits) - 1  # 0b1111
print(bin(n ^ mask))    #0b0101

x = 8
print(x << 1)
print(bin(x << 1))

x = 32
print(x >> 2)
print(bin(x >> 2))

a = 0b1101
b = 0b1011
print(bin(a ^ b))
print(a ^ b)