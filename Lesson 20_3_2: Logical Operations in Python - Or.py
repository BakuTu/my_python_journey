# Lesson 20_3_2: Logical Operations in Python - OR
# Practicing
# Date: 2025-08-02

# Import modules for working with time and logging
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - $(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

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
    '''
    Checks if only studying is possible if time is after 8 AM OR internet is available.

    Args:
    current_hor (int): Current hour (0-23).
    has_internet (bool): Internet availability (True/False).

    Returns:
    tuple: (bool, str) - (Can study, Reason key or None).
    '''
    if current_hour > 8 or has_internet:
        return True, None
    else:
        return False, "time_and_internet"

# Function to log the message for starting study
def start_study(lang=LANG_RU):
    '''
    Logs the message indicating online studying is possible.

    Args:
    lang (str): Language of the message('ru or 'en'). Defaults to 'ru'.
    '''
    messages = {
        LANG_RU: "Вы можете учиться онлайн!",
        LANG_EN: "You can study online!"
    }
    logger.info(messages.get(lang, messages[LANG_RU]))

# Function to log the reason for denial
def deny_study(reason_key, lang=LANG_RU):
    '''
    Logs the reason for denying study access.

    Args:
    reason_key (str): Key for the reason from reasons dictionary.
    lang (str): Language of the message ('ru' or 'en'). Defaults to 'ru'.

    Raises:
    If reason_key is not found in the reasons dictionary.
    '''
    if reason_key not in reasons:
        raise KeyError(f"Неверный ключ причины: {reason_key}. Доступные ключи: {list(reasons.keys())}")
    logger.info(reasons[reason_key][lang])

# Check if studying online is possible
current_hour = 7
has_internet = False

# Use the checking function and handle the result
can_study, reason_key = can_study_online(current_hour, has_internet)
if can_study:
    start_study(lang=LANG_EN)
else:
    deny_study(reason_key, lang=LANG_EN)
