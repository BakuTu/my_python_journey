# Lesson 20_1_3: Logical Operations in Python
# Practicing
# Date: 2025-07-17

# These variables simulate data that the backend might get from a database or from the user.

user_age = 15   # User age.
has_points = 100    # User's points.
has_subscription = False    # Does the user have an active subscription (True - yes, False - no).
is_blocked = False  # Is the user blocked (True - yes, False - no).

# Main video access check.
# If the user meets all criteria, they are granted access.

if user_age > 13 and (has_points >= 100 or has_subscription) and not is_blocked:
    print("Access Granted: you can watch the video.")
else:   # Block for cases where access is denied. If at least one condition in the main 'if' wasn't met, we enter here.
    if user_age <=13:   # First, we check if the user is too young.
        print("Access Denied: you are too young, age over 13 is required.")
# Then, if the user isn't young, we check if they have points OR a subscription.
# If points are less than 100 AND there's no subscription.
    elif has_points < 100 and not has_subscription:
        print("Access denied: 100+ points subscription required")
# If none of previous reason fit, it means the user is blocked.
    else:
        print("Access denied: you are blocked")



# Modify the code to grant access only at certain times (e.g. from 9 AM to 9 PM).

from datetime import datetime
# This variable simulate user data from a database.

user_age = 15
has_points = 101
has_subscription = True
is_blocked = False
current_hour = datetime.now().hour  # Current hour (0-23)

# Check video access.
if user_age > 13 and (has_points >= 100 or has_subscription) and not is_blocked and 9 <= current_hour <= 21:
    print("Access Granted: You can watch the video.")
else:   # If at least one condition fails, check the reason:
    if user_age <=13:   # If user is too young.
        print("Access Denied: You are too young, age over 13 is required.")
    elif has_points < 100 and not has_subscription: # If no points and no subscription.
        print("Access Denied: 100+ points or active subscription required.")
    elif is_blocked:    # If the user is blocked.
        print("Access Denied: You are blocked")
    else:   # If the reason inappropriate time:
        print("Access Denied: Video is only available between 9 AM and 9 PM.")



from datetime import datetime
user_age = 15
has_points = 101
has_subscription = True
is_blocked = False
current_hour = datetime.now().hour
if user_age > 13 and (has_points >= 100 or has_subscription) and not is_blocked and 7 <= current_hour <= 9:
    print("Access Granted: You can watch the video.")
else:
    if user_age <= 13:
        print("Access Denied: You are too young, age over 13 is required.")
    elif has_points < 100 and not has_subscription:
        print("Access Denied: 100+ points or active subscription required.")
    elif is_blocked:
        print("Access Denied: You are blocked.")
    else:
        print("Access Denied: Video is only available between 7 am and 9 am")



# Modify the code to allow access from 8 AM to 11 AM (inclusive) and test it at 10:04 AM
from datetime import datetime
user_age = 15
has_points = 1011
has_subscription = False
is_blocked = True
current_hour = datetime.now().hour

if user_age > 13 and (has_points >= 100 or has_subscription) and not is_blocked and 8 <= current_hour <= 11:
    print("Access Granted: You can watch the video")
else:
    if user_age <= 13:
        print("Access Denied: You are too young, age over 13 is required")
    elif has_points < 100 and not has_subscription:
        print("Access Denied: 100+ points or active subscription required.")
    elif is_blocked:
        print("Access Denied: You are blocked")
    else:
        print("Access Denied: Video available from 8 am to 11 am")



# Modify the code to allow access from 7:00 AM to 9:59 AM, considering not only hours but also minutes.

user_age = 17
has_points = 105
has_subscription = True
is_blocked = False
current_time = datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute

if user_age > 15 and (has_points >= 100 or has_subscription) and not is_blocked and (current_hour > 7 or (current_hour == 7 and current_minute >=0)) and (current_hour < 9 or (current_hour == 9 and current_minute <= 59)):
    print("Access Granted: You can watch the video.")
else:
    if user_age <= 13:
        print("Access Denied: You are too young, age over 13 is required")
    elif has_points < 100 and not has_subscription:
        print("Access Denied: 100+ points or active subscription is required")
    else:
        print("Access Denied: Video available between 7:00 AM and 9:59 AM")



from datetime import datetime
import pytz
user_age = 17
has_points = 101
has_subscription = True
is_blocked = False
timezone = pytz.timezone('Asia/Almaty')
current_hour = datetime.now(timezone).hour

if user_age > 13 and (has_points >= 100 or has_subscription) and not is_blocked and 9 <= current_hour <= 21:
    print("Access Granted: You can watch video")
else:
    if user_age <= 13:
        print("Access Denied: You are too young, age over 13 is required")
    elif has_points < 100 and not has_subscription:
        print("Access Denied: 100+ points or active subscription is required")
    elif is_blocked:
        print("Access Denied: You are blocked")
    else:
        print("Access Denied: Video available from 9 AM to 9 PM")

