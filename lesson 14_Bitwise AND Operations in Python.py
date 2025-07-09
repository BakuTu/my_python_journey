# Lesson 14: Bitwise AND Operations in Python
# Practicing
# Date: 2025-07-09

x1 = 2  # 010 in binary

y1 = 5  # 101 in binary

z1 = x1 & y1 # bitwise AND: 010 & 101 = 000

print(f"z1 = {z1}") # will print 0

print(f"z1 = {z1:0b}")



x2 = 4  # 100 in binary

y2 = 5 # 101 in binary

z2 = x2 & y2 # bitwise AND: 100 & 101 = 1000

print(f"z2 = {z2}") # will print 4

print(f"z2 = {z2:0b}")  # will print 100 (binary)


a = 6
b = 3
print(a & b)
print(bin(a & b))
print(f"z1 = {a} + {b}")
z1 = a & b
print(f"z1 = {z1}; z1 = {z1:0b}")



