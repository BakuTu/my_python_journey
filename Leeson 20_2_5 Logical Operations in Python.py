# Lesson 20_2_5: Logical Operations in Python
# Practicing
# Date: 2025-07-25

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
        reason_key (str): Key for the reason from the reasons dictionary.
        Language of the message. Defaults to 'en'.
    Raises:
        KeyError: If reason_key is not in the reasons dictionary.
    """
    if reason_key not in reasons:
        raise KeyError(f"Invalid reason key: {reason_key}. Available keys: {list(reasons.keys())}")
    print(reasons[reason_key][lang])

# Check if studying online is possible
current_hour = datetime.now().hour
has_internet = True

# Logic for checking conditions
if current_hour > 8 and has_internet:
    start_study(lang="en")
else:
    if current_hour <= 8 and not has_internet:
        deny_study("time_and_internet", lang="en")
    elif current_hour <= 8:
        deny_study("time_only", lang="en")
    else:
        deny_study("internet_only", lang="en")
