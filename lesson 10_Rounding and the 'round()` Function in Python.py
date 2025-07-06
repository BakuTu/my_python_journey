# Lesson 10_Rounding and the `round()` Function in Python
# Practicing
# Date: 2025-07-05

first_number = 2.0001
second_number = 5
third_number = first_number / second_number
print(third_number)

first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number))

first_number = 2.0001
second_number =0.1
third_number = first_number + second_number
print(round(third_number, 4))   # 2.1001

print(round(2.49))  # 2
print(round(2.51))  # 3

print(round(2.5))   # 2
print(round(3.5))   # 4

print(round(2.554, 2))  # 2.55
print(round(2.5551, 2)) # 2.56
print(round(2.554999, 2))   # 2.55
print(round(2.499, 2))  # 2.5

print(round(2.545, 2))  # 2.54
print(round(2.555, 2))  # 2.56
print(round(2.565, 2))  # 2.56
print(round(2.655, 2))  # 2.65
print(round(2.665, 2))  # 2.67
print(round(2.575, 2))  # 2.58

# Practicing

a = 5.555
b = 2
c = a + b
print(round(c, 1))  # 7.6

a = 10
b = 3
c = a / b
print(round(c, 3))  # 3.333

print(round(4.5))   # 4 It rounds to the nearest even number, so 4.5 becomes 4

