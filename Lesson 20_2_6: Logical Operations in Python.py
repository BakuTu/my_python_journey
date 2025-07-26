# Lesson 20_2_6: Logical Operations in Python
# Practicing
# Date: 2025-07-25

# Section of logic of checks and results

# Import module for working with time
from datetime import datetime

# Dictionary with reasons for denying study access
reasons = {
    "time_and_internet": {
        "ru": "Требуется время после 8 утра и подключение к интернету",
        "en": "Time after 8 AM and internet connection required"
    },
    "time_only": {
        "ru": "Требуется время после 8 утра",
        "en": "Time after 8 AM required"
    },
    "internet_only": {
        "ru": "Требуется подключение к интернету",
        "en": "Internet connection required"
    }
}

# Function to check if studying is possible
def can_study_online(current_hour, has_internet):
    """
    Checks if online studying is possible if time is after 8 AM and internet is available.

        Args:
            current_hour (int): Current hour (0-23).
            has_internet (bool): Internet availability (True/False).

        Returns:
            tuple: (bool, str) - (Can study, Reason key or None).
    """
    if current_hour > 8 and has_internet:
        return True, None
    elif current_hour <= 8 and not has_internet:
        return False, "time_and_internet"
    elif current_hour <= 8:
        return False, "time_only"
    else:
        return False, "internet_only"

# Function to print the message for starting study
def start_study(lang="en"):
    """
    Prints the message indicating online studying is possible.

    Args:
        lang (str): Language of the message. Defaults to "en".
    """
    messages = {
        "ru": "Вы можете учиться онлайн!",
        "en": "You can study online!"
    }
    print(messages.get(lang, messages["ru"]))

# Function to print the reason for denial
def deny_study(reason_key, lang="en"):
    """
    Prints the reason for denying study access.

    Args:
        reason_key (str): Key for the reason from reasons dictionary.
        lang (str): Language of the message. Defaults to "en".

    Raises:
        KeyError: If reason_key is not found in the reasons dictionary.
    """
    if reason_key not in reasons:
        raise KeyError(f"Invalid reason key: {reason_key}. Available keys: {list(reasons.keys())}")
    print(reasons[reason_key][lang])

# Check if studying online is possible
current_hour = datetime.now().hour
has_internet = True

# Use the checking function and handle the result
can_study, reason_key = can_study_online(current_hour, has_internet)
if can_study:
    start_study(lang="en")
else:
    deny_study(reason_key, lang="en")

# Test scenarios to verify the logic
test_cases = [
    (9, True, True, None, "You can study online!"),
    (7, False, False, "time_and_internet", "Time after 8 AM and internet connection required"),
    (7, True, False, "time_only", "Time after 8 AM required"),
    (9, False, False, "internet_only", "Internet connection required")
]
for hour, internet, expected_can_study, expected_reason, expected_output in test_cases:
    can_study, reason_key = can_study_online(hour, internet)
    output = reasons[reason_key]["en"] if reason_key else "You can study online!"
    print(f"Test: hour={hour}, internet={internet}, result={output}, expected={expected_output}")
    if output != expected_output:
        print(f"Error: expected '{expected_output}', got '{output}'")



