# Lesson 20_2_10: Logical Operations in Python
# Practicing
# Date: 2025-07-29

# Smart Home Condition Check for Turning on Lights

# These variables simulate data that the backend receives from smart home sensors (e.g.,IoT API).

current_time_is_evening = False # Is it evening now> (True/False)
room_is_dark = True #Is the room dark? (True/False)

# Functions for handling result.

def allow_turning_on_lights():
    print("Turning on lights in the room!")

def deny_turning_on_lights(reason):
    print(f"No need for lights: {reason}")

# Main logic checking conditions for lights
# If now evening AND in room dark, turn on lights.

if current_time_is_evening and room_is_dark:
    allow_turning_on_lights()
else:
    # Block for cases, when lights not needed (specifying reason)).
    if not current_time_is_evening:
        deny_turning_on_lights("It's not evening yet.")
    # Else, if evening has come (previous condition) was False, but in room not dark.
    elif not room_is_dark:
        deny_turning_on_lights("The room is bright enough.")

    # This 'else' will trigger, if for some other not accounted for reason lights not needed.
    # In such simple cases, it often indicates a logical error in coverage conditions,
    # But in complex systems can be useful as fallback for unforeseen situations.
    else:
        deny_turning_on_lights("Unknown reason. (Possibly an internal logic error.")
