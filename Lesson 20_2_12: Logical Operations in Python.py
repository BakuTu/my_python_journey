# Lesson 20_2_12: Logical Operations in Python
# Practicing
# Date: 2025-07-30

# Checking User Status for Sending a Notification
# The code determines whether it's needed to send a notification to a user if they are active AND allowed to receive notifications.

# Checking User Status for Sending a Notification

user_is_active = True   # Is the user currently online or active?
notifications_enabled = False # Has the user enabled notifications?

# If the user is active AND enabled notifications, we send
if user_is_active and notifications_enabled:
    print("Notification sent to user.")
else:
    print("Notification not sent (user is inactive or has disabled notifications).")