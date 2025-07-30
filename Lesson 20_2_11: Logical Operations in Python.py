# Lesson 20_2_11: Logical Operations in Python
# Practicing
# Date: 2025-07-29

# Dictionary for denial messages.
# This centralizes texts, which is convenient for their modification or translation.

reasons = {
    "not_evening": "No need for lights: it's evening yet.",
    "not_dark_room": "No need for lights: the room is bright enough",
    "unknown_reason": "No need for lights: unknown reason. (Possibly an internal logic error.)"
}

def allow_turning_on_lights():
    print("Turning on lights in the room!")

def deny_turning_on_lights(reason_key):
    print(reasons[reason_key])

current_time_is_evening = False
room_is_dark = True

# Main logic for checking light conditions.

if current_time_is_evening and room_is_dark:
    allow_turning_on_lights()
else:
    # Block for cases where lights are not needed (specifying the reason).
    if not current_time_is_evening:
        deny_turning_on_lights("not_evening")
    elif not room_is_dark:
        deny_turning_on_lights("not_dark_room")
    else:
        # Correction: The key "other" was changed to "unknown_reason" to match the key in the dictionary.
        deny_turning_on_lights("unknown_reason")
