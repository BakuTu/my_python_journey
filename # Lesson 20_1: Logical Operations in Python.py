# Lesson 20_1: Logical Operations in Python
# Practicing
# Date: 2025-07-16

user_age = 14   # sets the user’s age
has_points = 50 # sets the number of user points
has_subscription = False    # sets whether the user has a subscription
is_blocked = False  # sets whether the user is blocked
if user_age > 13 and (has_points >= 100 or has_subscription) and not is_blocked:    # checks all conditions for access
    print("Access granted: You can watch video")    # confirms successful access
else:   # executes the block if at least one condition fails
    if user_age <= 13:  # checks if the user is 13 or younger
        print("Access Denied: You are too young, age over 13 required") # informs about the age restriction
    elif has_points < 100 and not has_subscription: # checks if the user lacks points and a subscription
        print("Access Denied: 100+ points or active subscription required")
    else:   # handles the case where the user is blocked
        print("Access Denied: You are blocked")



user_age = 14
has_points = 100
has_subscription = False
is_blocked = False
username = "Anna"
if user_age > 13 and (has_points >= 100 or has_subscription) and not is_blocked and len(username) > 3:
    print("Access granted: You can watch the video")
else:
    if user_age <= 13:
        print("Access Denied: You are too young, age over 13 required")
    elif has_points < 100 and not has_subscription:
        print("Access Denied: 100+ points or active subscription required")
    elif is_blocked:
        print("Access Denied: You are blocked")
    else:
        print("Access Denied: The name is too short")



user_age = 59
has_points = 19
has_subscription = True
is_blocked = True
if not is_blocked and user_age > 13 and (has_points >= 100 or has_subscription):
    print("Access granted: You can watch the video")
else:
    if user_age <= 13:
        print("Access Denied: You are too young, age over 13 required")
    else:
        print("Access Denied: 100+ points or active subscription required")



user_age = 17   # This is a variable that stores the user's age.

if user_age > 13:   # If the condition is True, print this message.
    print("Access Granted")

else:   # If the condition is False, print this message.
    print("Access Denied")



# Example 1: Age verification (basic version)

user_age = 15   # We create the variable "user_age" and store the value 15.

if user_age > 13:   # If age greater than 13 - execute indented code.
    print("Access Granted")

else:   # Otherwise print denial message.
    print("Access Denial")



    # Example 2: Full access check (advanced version)

    # Create four 'boxes' with user data.

    user_age = 15   # Age
    has_subscription = False    # Subscription
    is_blocked = False  # Block status

    # Main check - all condition must be true

    if user_age > 13 and (has_points >= 100 or has_subscription) and not is_blocked:
        print("Access Granted: You can watch the video")

    else:   # If denied - specify the reason.
        if user_age <= 13:
            print("Access Denied: You are too young")
        elif has_points < 100 and not has_subscription:
            print("Access Denied: 100+ points or subscription")
        else:
            print("Access Denied: You are blocked")






