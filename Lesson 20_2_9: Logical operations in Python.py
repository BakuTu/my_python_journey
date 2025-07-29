# Lesson 20_2_9: Logical Operations in Python
# Practicing
# Date: 2025-07-29

# Smart Home Condition Check for Turning on Lights

current_time_is_evening = True  #Is it evening now? (True/False)
room_is_dark = True # Is the room dark? (True/False)

# If it's evening AND the room is dark, turn on the lights.

if current_time_is_evening and room_is_dark:
    print("Turning on the lights in the room!")
else:
    print("No need for lights (either it's still day, or it's bright enough)")

