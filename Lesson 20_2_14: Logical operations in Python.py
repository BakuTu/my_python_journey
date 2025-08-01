# Lesson 20_2_14: Logical Operations in Python
# Practicing
# Date: 2025-07-31

# Messages are now more specific and understandable

reasons = {
    "slot_not_free": "Cannot book patient: selected time slot is occupied.",
    "doctor_unavailable": "Cannot book patient: the doctor has other appointments at this time.",
    "unforeseen_circumstances": "Cannot book patient: due to unforeseen circumstances."
}

def allow_booking():
    print("Patient successfully booked for an appointment!")

def deny_booking(reason_key):
    print(reasons[reason_key])

time_slot_is_free = True
doctor_has_no_other_appointments = False

# Main logic for checking conditions for booking an appointment.

if time_slot_is_free and doctor_has_no_other_appointments:
    allow_booking()
else:
    # Block for cases where booking is impossible (specifying the reason).
    # Check if the reason for denial is that the time slot is occupied.
    if not time_slot_is_free:
        deny_booking("slot_not_free")
    # Else, if the slot is free, but the doctor already has other appointments.
    elif not doctor_has_no_other_appointments:
        # This condition now matches the key "doctor_unavailable".
        deny_booking("doctor_unavailable")
    # Fallback 'else' for any other (unforeseen) scenarios.
    else:
        deny_booking("unforeseen_circumstances")    # Key "unforeseen_reasons" changed to "unforeseen_circumstances" for more clarity.