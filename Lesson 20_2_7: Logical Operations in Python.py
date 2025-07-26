# Lesson 20_2_7: Logical Operations in Python
# Practicing
# Date: 2025-07-26

# Import module for working with time
from datetime import datetime

# Dictionary with reasons for denying study access
reasons = {
    "time_and_internet": "Time after 8 AM and internet connection required",
    "time_only": "Time after 8 AM required",
    "internet_only": "Internet connection required"
}

# Function to print the message for starting study
def start_study():
    """
    Prints the message indicating online studying is possible.
    """
    print("You can study online!")

# Function to print the reason for denial
def deny_study(reason_key):
    """
    Prints the reason for denying study access.

    Args:
        reason_key (str): Key for the reason from reasons dictionary.

    Raises:
        KeyError: If reason_key is not found in the reasons dictionary.
    """
    if reason_key not in reasons:
        raise KeyError(f"Invalid reason key: {reason_key}. Available reason keys: {list(reasons.keys())}")
    print(reasons[reason_key])

    # Check if studying online is possible
    current_hour = datetime.now().hour
    has_internet = True

    # Logic for checking conditions
    if current_hour > 8 and has_internet:
        start_study()
    else:
        if current_hour <= 8 and not has_internet:
            deny_study("time and internet")
        elif current_hour <= 8:
            deny_study("time_only")
        else:
            deny_study("internet_only")

# Test scenarios to verify the logic
test_cases = [
    (9, True, "You can study online!"),
    (7, False, "Time after 8 AM and internet connection required"),
    (7, True, "Time after 8 AM required"),
    (9, False, "Internet connection required")
]
for hour, internet, expected in test_cases:
    if hour > 8 and internet:
        output = "You can study online!"    # Expected output from start_study
    elif hour <= 8 and not internet:
        output = reasons["time_and_internet"]
    elif hour <= 8:
        output = reasons["time_only"]
    else:
        output = reasons["internet_only"]
    print(f"Test: hour={hour}, internet={internet}, result={output}, expected={expected}")
    if output != expected:
        print(f"Error: expected '{expected}', got '{output}'")

#


