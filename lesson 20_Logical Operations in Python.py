# Lesson 20: Logical Operations in Python
# Practicing
# Date: 2025-07-10

# We need to check that the user is older than 18 **and** has more than 100 likes to give access to premium features.

age = 20
likes = 130
if age > 18 and likes > 100:
    print("Access to premium future is allowed")
else:
    print("Access to premium future denied")

# Access will be given only if both conditions are True.



# We need to check if the user has a subscription **or** more than 500 likes to unlock a bonus.

has_subscription = False
likes = 550
if has_subscription or likes > 500: # We use 'or' to unlock the bonus if at least one condition is True.
    print("Bonus is open")
else:
    print("Bonus closed")



# We need to check that the user is **not banned** to allow login.

is_banned = False
if not is_banned:
    print("Entry permitted")
else:
    print("No Entry")

# We use 'not' to flip 'False' to 'True' if the user is not banned.



# Checking access to a paid article on the server.

# 1. Create a variable the user does not have a subscription yet.
has_subscription = True

# 2. Checking if there is a subscription.
if has_subscription:
    print("Access to the article is granted")
else:
    print("Subscribe to gain access")



# Checking access to premium API

has_subscription = False    # We create a variable that stores whether the user has a subscription. Currently, we set it to 'False', meaning there is no subscription.
if has_subscription:    # We check: if the user has a subscription (has_subscription == True), we execute the code under this condition.
    print("Access to the premium API granted")  # If the condition is True, we print that access to the premium API is granted.
else:   # If the condition is False (has_subscription == False) the code under 'else' is executed.
    print("Access to premium API denied")   # Since we have 'False', this line is executed, and we print that access to the premium API is denied.



# Checking User Subscription Status in Real Applications

# Simulation of data from the database
user_data = {
    "username": "John Doe",
    "has_subscription": True
}
# Checking access
if user_data["has_subscription"]:
    print("User can access premium content")
else:
    print("User cannot access premium content")



# Let’s check if the user has a subscription **and** enough credits to access a paid API.

has_subscription = True # Create a variable showing that the user has a subscription.
credits = 30    # We set the user's credit amount.
if has_subscription and credits >= 30:  # We check two conditions: the user has a subscription and has 30 or more credits.
    print("Access to API granted")  # If both condition are True, we print "Access to API granted"
else:
    print("Access to API denied")   # If at least one condition is False, we print "Access to API denied".



# Checking Premium Subscription or View Count to Unlock Bonus Content

is_premium = False  # We indicate that the user doesn't have a premium subscription
views = 1000    # We set the number of views.
if is_premium or views > 1000:   # We check if the user has premium or more than 1000 views.
    print("Bonus content unlocked") # If at least one condition is True, we print "Bonus content unlocked"
else:
    print("Bonus content unavailable")  # if both condition are False, we print "Bonus content unavailable".



# Checking If User Is Not Banned Before Allowing Forum Comments

is_banned = False # We indicate that the user is not banned.
if not is_banned:   # We use 'not' to check that 'is_banned' is 'False'.
    print("Commenting is allowed")  # if 'not is_banned' is 'True' we print 'Commenting is allowed'.
else:
    print("You are banned, commenting is prohibited")   # If the user is banned (is_banned = True), we print "You are banned, commenting is prohibited".



# Write code that checks if the user is over 13 **and** has a subscription to watch a video.

user_age = 16
has_subscription = True
if user_age > 13 and has_subscription:
    print("The video is available for viewing")
else:
    if user_age <= 13:
        print("No entry: You are to young")
    else:
        print("No entry: Subscription required")



# Checking If User Is Over 13 and Has Subscription to Watch Video

user_age = 17
has_subscription = False
if user_age >= 17 and has_subscription:
    print("Access granted: You can watch the video")
else:
    if user_age < 17:
        print("Request rejected: You are too young. Age verification required")
    else:
        print("Request rejected: Please check your subscription")



user_age = 17    # Sets a variable for user's age.
has_subscription = True # Sets a variable indicating whether the user has a subscription
is_blocked = False # Sets a variable indicating whether the user is blocked.
if user_age > 13 and has_subscription and not is_blocked:   # Checks three conditions to grant access.
    print("Access granted: You can watch video")   # Prints a message if all conditions are met.
else:   # Executes the block if at least one condition in the 'if' fails.
    if user_age <= 13:  # Checks if the user is 13 or younger.
        print("Access Denied: You are too young")   # Informs that the user is too young.
    elif not has_subscription:  # Checks if the user lacks a subscription if the age is fine.
        print("Access Denied: Active Subscription Required")    # Informed that a subscription is required.
    else:
        print("Access Denied: You are blocked")



user_age = 18
has_subscription = True
is_banned = True
if user_age > 13 and has_subscription and not is_banned:
    print("Access granted: You can watch video")
else:
    if user_age <= 13:
        print("Access Denied: You are too young")
    elif not has_subscription:
        print("Access Denied: Active Subscription Required")
    else:
        print("Access Denied: You are blocked")



# Modify the code to grant access if the user is over 13 and has 100 points, even without a subscription, and is not blocked.

user_age = 120
has_subscription = True
is_blocked = False
points = 50
if user_age > 13 and (has_subscription or points >= 100) and not is_blocked:
    print("Access granted: You can watch video")
else:
    if user_age <= 13:
        print("Access Denied: You are too young")
    elif not has_subscription and points < 100:
        print("Access Denied: Subscription or 100 points required")
    else:
        print("Access Denied: You are blocked")



user_age = 15
has_subscription = False
is_blocked = True
if not is_blocked and user_age > 13 and not has_subscription:
    print("Access granted: You can watch video")
else:
    if is_blocked:
        print("Access Denied: You are blocked")
    elif user_age <= 13:
        print("Access Denied: You are too young")
    else:
        print("Access Denied: Active Subscription Required")




user_age = 15   # User's age 15
has_points = 100    # User has 100 points
has_subscription = False    # User does not have a subscription 'False'
is_blocked = False  # User is not blocked

# Chek: user is over 13, has points 100 points or subscription, and is not blocked.

if user_age > 13 and (has_points >= 100 or has_subscription) and not is_blocked:
    print("Access granted: You can watch video")   # If all condition are met, print "Access granted".
else:
    if user_age <= 13:
        print("Access Denied: You are too young")   # If user is too young, print this.
    elif has_points < 100 and not has_subscription: # If user has no points and no subscription, print this.
        print("Access Denied: Need 100+ points or Subscription")
    elif is_blocked:
        print("Access Denied: You are blocked") # If user blocked print this.
    else:
        print("Access Denied: Other reason")    # Default fallback other denial reason.





















