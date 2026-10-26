# Terminal Record: Harvest Table Catering

## 1. Building the project

```
cd ~/Desktop
mkdir ism3232-midterm
cd ism3232-midterm
git init
git branch -m main
/usr/bin/python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
touch business_rules.py main.py commands.md README.md
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
echo ".venv/" > .gitignore
echo "__pycache__/" >> .gitignore
pip freeze > requirements.txt
git add .
git status
git commit -m "Set up midterm project structure"
git remote add origin https://github.com/aayushiyerusf/ism3232-midterm.git
printf "protocol=https\nhost=github.com\n" | git credential reject
gh auth switch --user aayushiyerusf
gh auth setup-git
git push -u origin main
```

## 2. The virtual environment

```
which python3
```

```
/Users/aayushiyer/Desktop/ism3232-midterm/.venv/bin/python3
```

The path ends in `.venv/bin/python3`, which shows that python3 is coming from the project's virtual environment.

## 3. The project structure

```
tree -L 2
```

```
.
├── README.md
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_business_rules.py

2 directories, 7 files
```

The `.venv` folder is on my computer but not in my GitHub repository, because `.gitignore` keeps it out (tree hides it because its name starts with a dot).

## 4. Every function and test

```
rg 'def '
```

```
business_rules.py
22:def calculate_food_cost(guest_price: float, guests: int) -> float:
27:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
36:def calculate_event_total(
48:def needs_signoff(total: float) -> bool:
53:def needs_second_chef(guests: int, total: float) -> bool:
58:def total_booked(events: list) -> float:
68:def largest_event(events: list) -> str:
82:def format_event_line(

tests/test_business_rules.py
16:def test_food_cost_is_price_times_guests():
21:def test_discount_24_guests_is_none():
25:def test_discount_25_guests_is_five_percent():
29:def test_discount_99_guests_nonprofit_is_five_percent():
33:def test_discount_100_guests_nonprofit_is_twelve_percent():
38:def test_discount_100_guests_not_nonprofit_is_five_percent():
42:def test_nonprofit_true_changes_event_total():
48:def test_fee_added_when_cost_is_exactly_500():
52:def test_fee_not_added_when_cost_is_500_01():
56:def test_event_total_with_discount_and_no_fee():
61:def test_no_signoff_at_exactly_2500():
65:def test_signoff_at_2500_01():
70:def test_no_second_chef_at_80_guests_low_total():
74:def test_second_chef_at_81_guests_low_total():
78:def test_no_second_chef_at_2999_99_few_guests():
82:def test_second_chef_at_exactly_3000_few_guests():
87:def test_total_booked_adds_two_events():
95:def test_total_booked_empty_list_is_zero():
100:def test_largest_event_returns_biggest_client():
108:def test_largest_event_tie_returns_first():
116:def test_largest_event_empty_list_returns_empty_string():
121:def test_format_line_no_and_no():
126:def test_format_line_yes_and_yes_two_decimals():
```

`business_rules.py` defines 8 functions and `tests/test_business_rules.py` defines 23 tests.

## 5. Which files print

```
rg -l 'print'
```

```
main.py
README.md
```

`main.py` is the only Python file that prints, and `business_rules.py` is not listed because its functions return values instead of printing them.

## 6. The commit history

```
git log --oneline
```

```
PASTE OUTPUT HERE
```

There were 8 commits at that point.