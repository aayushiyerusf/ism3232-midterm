"""Tests for the Harvest Table Catering business rules."""

from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)


# Rule 1: food cost
def test_food_cost_is_price_times_guests():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


# Rule 2: discount tiers (limit at 25 and at 100)
def test_discount_24_guests_is_none():
    assert get_event_discount(24) == 0.0


def test_discount_25_guests_is_five_percent():
    assert get_event_discount(25) == 0.05


def test_discount_99_guests_nonprofit_is_five_percent():
    assert get_event_discount(99, True) == 0.05


def test_discount_100_guests_nonprofit_is_twelve_percent():
    assert get_event_discount(100, True) == 0.12


# Rule 3: 12% is only for nonprofits
def test_discount_100_guests_not_nonprofit_is_five_percent():
    assert get_event_discount(100, False) == 0.05


def test_nonprofit_true_changes_event_total():
    assert round(calculate_event_total(25.00, 150, True), 2) == 3300.00
    assert round(calculate_event_total(25.00, 150, False), 2) == 3562.50


# Rule 4: service fee (limit at $500)
def test_fee_added_when_cost_is_exactly_500():
    assert round(calculate_event_total(500.00, 1), 2) == 575.00


def test_fee_not_added_when_cost_is_500_01():
    assert round(calculate_event_total(500.01, 1), 2) == 500.01


def test_event_total_with_discount_and_no_fee():
    assert round(calculate_event_total(30.00, 120), 2) == 3420.00


# Rule 5: manager sign-off (limit at $2,500)
def test_no_signoff_at_exactly_2500():
    assert needs_signoff(2500.00) is False


def test_signoff_at_2500_01():
    assert needs_signoff(2500.01) is True


# Rule 6: second chef (limits at 80 guests and $3,000)
def test_no_second_chef_at_80_guests_low_total():
    assert needs_second_chef(80, 100.00) is False


def test_second_chef_at_81_guests_low_total():
    assert needs_second_chef(81, 100.00) is True


def test_no_second_chef_at_2999_99_few_guests():
    assert needs_second_chef(10, 2999.99) is False


def test_second_chef_at_exactly_3000_few_guests():
    assert needs_second_chef(10, 3000.00) is True


# total_booked
def test_total_booked_adds_two_events():
    events = [
        {"client": "Small", "guest_price": 18.00, "guests": 20, "nonprofit": False},
        {"client": "Big", "guest_price": 30.00, "guests": 120, "nonprofit": False},
    ]
    assert round(total_booked(events), 2) == 3855.00


def test_total_booked_empty_list_is_zero():
    assert round(total_booked([]), 2) == 0.00


# largest_event
def test_largest_event_returns_biggest_client():
    events = [
        {"client": "Small", "guest_price": 18.00, "guests": 20, "nonprofit": False},
        {"client": "Big", "guest_price": 30.00, "guests": 120, "nonprofit": False},
    ]
    assert largest_event(events) == "Big"


def test_largest_event_tie_returns_first():
    events = [
        {"client": "First", "guest_price": 18.00, "guests": 20, "nonprofit": False},
        {"client": "Second", "guest_price": 18.00, "guests": 20, "nonprofit": False},
    ]
    assert largest_event(events) == "First"


def test_largest_event_empty_list_returns_empty_string():
    assert largest_event([]) == ""


# format_event_line
def test_format_line_no_and_no():
    line = format_event_line("Finch Law", 435.00, False, False)
    assert line == "Finch Law: $435.00 | sign-off: no | second chef: no"


def test_format_line_yes_and_yes_two_decimals():
    line = format_event_line("Island Pantry", 3300, True, True)
    assert line == "Island Pantry: $3300.00 | sign-off: yes | second chef: yes"
