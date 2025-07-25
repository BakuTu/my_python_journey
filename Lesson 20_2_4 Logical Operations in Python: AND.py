# Lesson 20_1_3: Logical Operations in Python: AND
# Practicing
# Date: 2025-07-19

age = 22
weight = 58
result = age > 21 and weight == 58
print(result)



result = 4 and "w"
print(result)


result = 0 and "w"
print(result)



# To work, you need to define user as a dictionary

user = {
    'is_active': True,
    'has_subscription': False
}

def allow_access():
    print("Access allowed")

def deny_access():
    print("Access denied")

if user['is_active'] and user['has_subscription']:
    allow_access()
else:
    deny_access()



x = 5
y = 10
if x > 3 and y == 10:
    print("Condition is done")


a = 0
b = 'Hello'
result = a and b
print(result)

a = 1
b = 'Hello World'
result = a and b
print(result)



user = {
    'is_active': True,
    'has_subscription': True
}

def allow_access():
    print("Access Granted")

def deny_access():
    print("Access Denied")

if user['is_active'] and user['has_subscription']:
    allow_access()
else:
    deny_access()



    # Write code that checks if the user is over 18 and has a subscription. If both are true, print “Welcome!”.

user = 19
has_subscription = True
if user > 18 and has_subscription:
    print("Welcome")
else:
    print("Access Denied: age over 18 is required")



# Write code that checks if the user has 50+ points or a subscription. If at least one is true, print “Access granted”.

has_subscription = False
has_points = 6
if has_subscription or has_points > 50:
    print("Wellcome")
else:
    print("Access Denied: 50+ points or active subscription is required")


# Write code that checks if the user is not blocked. If not blocked, print “You can log in”.

user = "Antony"
is_blocked = True
if not is_blocked:
    print("You can log in")
else:
    print("You can't log in")


# The code checks if a student can get praise if they have both a 5 in math and a 5 in literature.

math_grade = 5
literature_grade = 5
if math_grade == 5 and literature_grade == 5:
    print("Well done, you got price!")
else:
    print("Try harder, you need a 5 in both math and literature")



# The code checks if an order can be shipped if the item is in stock and the user has paid.

item_in_stock = True
payment_received = False

if item_in_stock and payment_received:
    print("Order shipped!")
else:
    print("Order not shipped: check item availability or payment")


age = 22
weight = 58
result = age > 21 and weight == 58
print(result)


# The code checks if you can go for a walk if it’s after 3 PM and the weather is good.

from datetime import datetime

# Checking time and weather for a walk

current_hour = datetime.now().hour
is_good_weather = True

if current_hour > 15 and is_good_weather:
    print("You can go for a walk!.")
else:
    print("Stay home: it's either too early or bad weather.")



    # Write code to check if you can borrow a book if it’s available in the library 'and' you have a library card.

    book_available = True
    has_library_card = True
    if book_available and has_library_card:
        print("You can borrow a book")
    else:
        print("Book is not available in the library")



book_available = False
has_library_card = False
if book_available and has_library_card:
    print("Book borrowed")
else:
    if not book_available:
        print("Book is not available in the library.")
    elif not has_library_card:
        print("You don't have library card.")


age = 14
has_money = False

if age > 12 and has_money:
    print("Ticket bought!")
else:
    if age <= 12:
        print("You are too young, age over 12 required.")
    else:
        print("You don't have money to buy ticket.")



# Checking if a lesson can start

def start_lesson():
    print("The lesson has begun!")

def cancel_lesson(reason):
    print(f"Lesson cannot start: {reason}")

teacher_present = False
all_students_present = True

if teacher_present and all_students_present:
    start_lesson()
else:
    if not teacher_present and not all_students_present:
        cancel_lesson("Teacher and students are absent")
    elif not teacher_present:
        cancel_lesson("Teacher is absent")
    else:
        cancel_lesson("Students are absent")



# Write code with borrow_book() and deny_book(reason) functions to check if a book can be borrowed if it’s not reserved and the library is open.

# Checking if a book can be borrowed from the library

def borrow_book():
    print("Book is borrowed!")

def deny_book(reason):
    print(f"Cannot borrow book: {reason}")

book_not_reserved = True
library_open = True

if book_not_reserved and library_open:
    borrow_book()
else:
    if not book_not_reserved and not library_open:
        deny_book("Book is reserved and library is closed")
    elif not book_not_reserved:
        deny_book("Book is reserved")
    else:
        deny_book("Library is closed")


# Write code with start_lesson() and cancel_lesson(reason) functions to check if a lesson can start if the teacher is present and the projector is working.

# Checking if a lesson can start

def start_lesson():
    print("The lesson has begun!")

def cancel_lesson(reason):
    print(f"Lesson cannot start because: {reason}")

reasons = {
    "both": "The teacher is absent and the projector is not work"
    "teacher",
    "teacher": "The teacher is absent",
    "projector": "The projector is not work"
}

teacher_is_present = False
projector_is_working = True

if teacher_is_present and projector_is_working:
    start_lesson()
else:
    if not teacher_is_present and not projector_is_working:
        cancel_lesson(reasons["both"])
    elif not teacher_is_present:
        cancel_lesson(reasons["teacher"])
    else:
        cancel_lesson(reasons["projector"])



# Write code with start_stream() and stop_stream(reason) functions, using a reasons dictionary, to check if a stream can start if the internet is working and the camera is on.

# Checking if stream can start

def start_stream():
    print("Stream started!")

def stop_stream(reason):
    print(f"Stream cannot start because: {reason}")

reasons = {
    "no_internet_and_camera": "The internet is not working and camera is off",
    "internet": "The internet is not working",
    "camera": "The camera is not working"
}

internet_is_working = False
camera_is_on = False

if internet_is_working and camera_is_on:
    start_stream()
else:
    if not internet_is_working and camera_is_on:
        stop_stream(reasons["no_internet_and_camera"])
    elif not internet_is_working:
        stop_stream(reasons["internet"])
    else:
        stop_stream(reasons["camera"])




# Write code with watch_video() and deny_video(reason) functions, using a reasons dictionary, to check if a video can be watched if it’s after 10 AM and there’s a subscription.

from datetime import datetime
current_hour = datetime.now().hour
has_subscription = True

def watch_video():
    print("Video started!")

def deny_video(reason):
    print(f"Video is not available because: {reason}")

reasons = {
    "no_time_no_sub": "not after 10 AM and no subscription",
    "no_time": "Not after 10 AM",
    "no_sub": "No subscription"
}

if current_hour > 10 and has_subscription:
    watch_video()
else:
    if not current_hour > 10 and not has_subscription:
        deny_video(reasons["no_time_no_sub"])
    elif not current_hour > 10:
        deny_video(reasons["no_time"])
    else:
        deny_video(reasons["no_sub"])



# Import libraries for testing and working with time

import unittest
from unittest.mock import patch
from datetime import datetime

# Main code for testing

def watch_video():
    print("Video started!")

def deny_video(reason):
    print(f"Video is not available because: {reason}")

# Dictionary of denial reasons

reasons = {
    "no_time_no_sub": "not after 10 AM and no subscription",
    "no_time": "not after 10 AM",
    "no_sub": "no subscription"
}

# Class for testing video access logic

class TestVideoAccess(unittest.TestCase):   # Test for when both conditions are true (time after 10 AM and subscription exists)
    @patch('builtins.print')
    def test_both_conditions_true(self, mock_print):
        current_hour = 11
        has_subscription = True
        if current_hour > 10 and has_subscription:
            watch_video()
        else:
            deny_video(reasons["no_time_no_sub"])
        mock_print.assert_called_with("Video started!")

# Test fo when both conditions are false (time before 10 AM and no subscription)
    @patch('builtins.print')
    def test_no_time_no_subscription(self, mock_print):
        current_hour = 9
        has_subscription = False
        if current_hour > 10 and has_subscription:
            watch_video()
        else:
            deny_video(reasons["no_time_no_sub"])
        mock_print.assert_called_with("Video is not available because: not after 10 AM and no subscription")

# Run tests if the file is executed directly

if __name__ == '__main__':
    unittest.main()



# Write code to check if you can study online if it’s after 8 AM and there’s internet.

# Import module for working with time
from datetime import datetime

# Get the current hour and check internet availability
current_hour = datetime.now().hour
has_internet = True

# Check if studying online is possible (time after 8 AM and internet available)
if current_hour > 8 and has_internet:
    print("You can study online!")
else:
    if current_hour <= 8 and not has_internet:
        print("Time after 8 AM and internet connection required")
    elif current_hour <= 8:
        print("Time after 8 AM required")
    else:
        print("Internet connection required")



# If the task only requires checking conditions without detailed messages, the code can be simplified

# Import module for working with time
from datetime import datetime

# Get the current hour and check internet availability
current_hour = datetime.now().hour
has_internet = False

# Check if studying online is possible (time after 8 AM and internet available)
if current_hour > 8 and has_internet:
    print("You can study online!")
else:
    print("You cannot study online.")


# Import module for working with time
from datetime import datetime

# Function to check access to online studying

# Import module for working with time
from datetime import datetime

# Function to check access to online studying
def can_study_online(current_hour, has_internet):
# Check if both conditions are met: time after 8 AM and internet available
    if current_hour > 8 and has_internet:
        return True, "You can study online!"
# If both conditions are false: time is before or at 8 AM and no internet
    elif current_hour <= 8 and not has_internet:
        return False, "Time after 8 AM and internet connection required"
# If only the time is incorrect (before or at 8 AM)
    elif current_hour <= 8:
        return False, "Time after 8 AM required"
# If only internet is missing (time after 8 AM)
    else:
        return False, "Internet connection required"

# Get the current hour and set internet availability
current_hour = datetime.now().hour
has_internet = True

# Call the function and handle the result
can_study, message = can_study_online(current_hour, has_internet)
print(message)

# Simple test to verify the function
test_cases = [
    (9, True, "You can study online!"), # After 8 AM, Internet available
    (7, False, "Time after 8 AM and internet connection required"), # Before 8 AM, internet available
    (7, True, "Time after 8 AM required"), # Before 8 AM, internet available
    (9, False, "Internet connection required") # After 8 AM, no internet
]

for hour, internet, expected in test_cases:
    can_study, message = can_study_online(hour, internet)
    print(f"TestCase: hour={hour}, internet={internet}, result={message}, expected={expected}")
    if message != expected:
        print(f"Error in TestCase: expected '{expected}', got '{message}'")




































