# Lesson 20_1_2: Logical Operations in Python
# Practicing
# Date: 2025-07-17

# Analysis of the 'check_access' function.

# Step 1: Declare a function (logic check only)

def check_access(user):
    if user["age"] > 13 and (user["points"] >= 100 or user["subscription"]) and not user["blocked"]:
        return "Access Granted"
    else:
        return "Access Denied"


# Step 2: Create data (Separate from the function).

my_user = {
    "age": 15,
    "points": 120,
    "subscription": False,
    "blocked": False
}

# Step 3: Call the function and print the result.
print(check_access(my_user))



# 1
def check_access(user):
    if user["age"] > 18 and (user["points"] >= 100 or user["subscription"]) and not user["blocked"]:
        return "Access Granted"
    else:
        return "Access Denied"

# 2
my_user = {
    "age": 19,
    "points": 99,
    "subscription": False,
    "blocked": False
}

# 3
print(check_access(my_user))

# Other verse:

def check_access(user):
    age_ok = user["age"] > 13
    points_ok = user["points"] >= 100
    has_sub = user["subscription"]
    not_banned = not user["blocked"]

    if age_ok and (points_ok or has_sub) and not not_banned:
        return "Access Granted"
    else:
        return "Access Denied"