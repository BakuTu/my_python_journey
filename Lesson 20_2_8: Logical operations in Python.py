# Lesson 20_2_8: Logical Operations in Python
# Practicing
# Date: 2025-07-26

# Checking event ticket availability

# These variables simulate data that the backend receives from the booking system and user profile.

tickets_available = 5  # Number of remaining tickets (changed to 0 for testing).
budget = 1000    # Your budget for the ticket.
ticket_price = 1200  # Price of one ticket.


# Functions to handle the result.

def allow_purchase():
    print("Greate! The ticket can be bought.")

def deny_purchase(reason):
    print(f"Ticket unavailable: {reason}")


# Main access check logic.

# If tickets are available AND the budget allows, we allow the purchase.

if tickets_available > 0 and budget >= ticket_price:
    allow_purchase()
else:

    # Block for cases where purchases is denied (specifying the reason).

    # Check if tickets are available.

    if tickets_available <=0:
        deny_purchase("No available seats.")

    # Else, if tickets are available, but not enough money.

    elif budget < ticket_price:
        deny_purchase("Not enough monet to purchase.")

    # This 'else' will trigger if access is denied for some other reason not yet accounted for.
    # For example, in the future, a "user blocked" condition might be added.

    else:
        deny_purchase("Unknown reason for denial. (Possibly an internal system error).")