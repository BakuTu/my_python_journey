# Lesson 20_2_13: Logical Operations in Python
# Practicing
# Date: 2025-07-30

# Dictionary for denial messages.

reasons = {
    "no_active": "Notification not sent: User is inactive.",
    "no_notifications_enabled": "Notification not sent: User has disabled notifications.",
    # Adding a key for "unknown reason" denial.
    "unknown_reason": "Notification not sent: Unknown reason for denial. (Possibly a system error)"
}

def allow_send_notification():
    print("Notification sent to User!")

def deny_send_notification(reason_key):
    print(reasons[reason_key])

user_is_active = False  # Is user active? (True/False)
notifications_enabled = False    # Are notifications enabled? (True/False)

# Main logic for checking conditions for sending a notification.

if user_is_active and notifications_enabled:
    allow_send_notification()
else:
    # Block for cases where the notification is not sent (specifying the reason).
    if not user_is_active:
        deny_send_notification("no_active")
    # Else, if the user is active, but notifications are disabled.
    elif not notifications_enabled:
        deny_send_notification("no_notifications_enabled")
        # Correction: The key in the dictionary was "no_notifications_enabled",not "no_notification".
        # Fallback 'else' for any other (unforeseen) scenarios.
    else:
        deny_send_notification("unknown_reason")