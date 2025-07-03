#   Lesson 05_Dynamic Typing in Python
#   Practicing
#   Date: 2025-07-03

userId = "abc"  # assign a string, so type is str
print(userId)   # print the value

userId = 234    # now assign an integer, so type becomes int
print(userId)   # print the new value

userId = "abc"  # assign a string
print(type(userId)) #check the type, it will show <class 'int'>

userId = 234    # assign an integer
print(type(userId)) # check the type, it will show <class 'int'>