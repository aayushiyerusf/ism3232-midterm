"""Business rules for Harvest Table Catering."""

# Discount tiers (rules 2 and 3)
MEDIUM_EVENT_GUESTS = 25
LARGE_EVENT_GUESTS = 100
NO_DISCOUNT = 0.0
MEDIUM_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12

# Service fee (rule 4)
SERVICE_FEE = 75.00
SERVICE_FEE_LIMIT = 500.00

# Manager sign-off (rule 5)
SIGNOFF_LIMIT = 2500.00

# Second chef (rule 6)
SECOND_CHEF_GUESTS = 80
SECOND_CHEF_TOTAL = 3000.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Return the food cost before any discount."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate as a decimal for this event."""
    if guests >= LARGE_EVENT_GUESTS and nonprofit:
        return NONPROFIT_DISCOUNT
    if guests >= MEDIUM_EVENT_GUESTS:
        return MEDIUM_DISCOUNT
    return NO_DISCOUNT