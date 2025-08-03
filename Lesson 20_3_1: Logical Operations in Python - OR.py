# Lesson 20_3_!: Logical Operations in Python - OR
# Practicing
# Date: 2025-08-01

# Import module for working with time
from datetime import datetime

# Language constants
LANG_RU = "ru"
LANG_EN = "en"

# Dictionary with reasons for denying study access
reasons = {
    "time_and_internet": {
        LANG_RU: "Требуется время после 8 утра и подключение к интернету",
        LANG_EN: "Time after 8 AM and internet connection required"
    },
    "time_only": {
        LANG_RU: "Требуется время после 8 утра",
        LANG_EN: "Time after 8 AM required"
    },
    "internet_only": {
        LANG_RU: "Требуется подключение к интернету",
        LANG_EN: "Internet connection required"
    }
}

# Function to check if studying is possible
def can_study_online(current_hour, has_internet):
    """
    Checks if online studying is possible if time is after 8 AM OR internet is available.

    Args:
    current_hour (int): Current hour (0-23).
    has_internet (bool): Internet availability (True/False).

    Returns:
    tuple: (bool, str) - (Can study, Reason key or None).
    """
    if current_hour > 8 or has_internet:
        return True, None
    else:
        return False, "time_and_internet"

# Function to print the message for starting study
def start_study(lang=LANG_RU):
    """
    Pints the message indicating online studying is possible.

    Args:
    lang (str). Language of the message ('ru' or 'en'). Defaults to 'ru'.
    """
    messages = {
        LANG_RU: "Вы можете учиться онлайн!",
        LANG_EN: "You can study online!"
    }
    print(messages.get(lang, messages[LANG_RU]))

# Function to print the reason for denial
def deny_study(reason_key, lang=LANG_RU):
    """
    Prints the reason for denying study access.

    Args:
    reason_key (str): Key for the reason from the reasons dictionary.
    lang (str): Language of the message ('ru' or 'en'). Defaults to 'ru'.

    Raises:
    KeyError: If reason_key is not found in the reasons dictionary.
    """
    if reason_key not in reasons:
        raise KeyError(f"Неверный ключ причины: {reason_key}. Доступные ключи: {list(reasons.keys())}")
    print(reasons[reason_key][lang])

# Check if studying online is possible
current_hour = datetime.now().hour
has_internet = True

# Use the checking function and handle the result
can_study, reason_key = can_study_online(current_hour, has_internet)
if can_study:
    start_study(lang=LANG_RU)
else:
    deny_study(reason_key, lang=LANG_RU)



