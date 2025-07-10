# Lesson 19: Conditional Expressions and Boolean Values in Python
# Practicing
# Date: 2025-07-10

x = 7
y = 5
result = x > y
print(result)

a = 5
b = 3
print(a > b)    # true
print(a == b)   # false
print(a != b)   # true

a = 10
b = 20
if a < b:
    print("a less than b")
else:
    print("a not less than b")


# Comparison operations

a = 5
b = 6
result = 5 == 6
print(result)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
bool1 = True
bool2 = False
print(bool1 == bool2)


temperature = 32
if temperature > 30:
    print("I wear T-shirt")
else:
    print("I wear a jacket")


user_balance = 1000
item_price = 1200
if user_balance >= item_price:
    print("The purchase was successful")
else:
    print("Insufficient funds")


user_age = 25
if user_age >= 18:
    print("Access granted")
else:
    print("Access denied")


a = "My name is Make"
b = "My name is Aibeke"
print(a == b)



number_of_likes = 1000
if number_of_likes >= 100:
    print("Popular post")
else:
    print("Regular post")



