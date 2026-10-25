# ISM3232 Midterm: Harvest Table Catering

- **Name:** Aayush Iyer
- **Version:** 1.0
- **Date:** October 25, 2026

## What This Program Does

This program prices catering events for Harvest Table Catering. For each event it works out the food cost, applies the right guest discount, and adds a service fee for small events. It then flags which events need a manager's sign-off or a second chef and prints a report with totals for all eight events.

## Business Rules

1. Food cost is the price per guest multiplied by the number of guests.
2. Events with fewer than 25 guests get no discount, 25 to 99 guests get 5% off, and 100 or more guests get 12% off.
3. The 12% discount is only for registered nonprofits; other events with 100 or more guests get 5% off.
4. A $75 service fee is added when the cost after the discount is $500 or less.
5. An event total over $2,500 needs a manager's sign-off.
6. An event needs a second chef if it has more than 80 guests or its total is $3,000 or more.

## How to Run

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

```
ruff check .
pytest -v
```

I wrote 23 tests, and all of them pass.

## Files in This Repository

- `business_rules.py`: the eight functions that apply the business rules
- `main.py`: the list of events and the code that prints the report
- `commands.md`: my terminal record of building and checking the project
- `README.md`: this file, explaining what the project does and how to use it
- `requirements.txt`: the Python packages the project needs, from `pip freeze`
- `.gitignore`: keeps `.venv/` and `__pycache__/` out of the repository
- `tests/__init__.py`: an empty file that makes `tests` a Python package
- `tests/test_business_rules.py`: the pytest tests for every function and rule limit

## AI Use Statement

I did not use any form of AI to complete this exam.