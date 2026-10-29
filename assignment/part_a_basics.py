"""
Part A — Variables, operators, strings and conditionals (Class 1)

Replace each `pass` with your code. Every function must RETURN its answer
(not print it). Do not change the function names or parameters.

Check your work any time with:   pytest tests/test_part_a.py
"""


def celsius_to_fahrenheit(celsius):
    """A1. Convert a temperature from Celsius to Fahrenheit.

    Formula: F = C × 9/5 + 32

    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit(0)
    32.0
    """
    pass


def is_even(number):
    """A2. Return True if `number` is even, False if it is odd.

    Hint: the remainder operator %.

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    """
    pass


def get_grade(mark):
    """A3. Return the letter grade for a mark out of 100.

    70–100 → "A"
    60–69  → "B"
    50–59  → "C"
    40–49  → "D"
    0–39   → "E"
    Below 0 or above 100 → "Invalid"

    >>> get_grade(74)
    'A'
    >>> get_grade(105)
    'Invalid'
    """
    pass


def ticket_price(age, is_student):
    """A4. Return the cinema ticket price in KES.

    Rules (check them in this order):
    - Under 5 years old             → 0   (free)
    - 5 to 17 years old             → 300
    - 65 or older                   → 400
    - 18 to 64 AND a student        → 500
    - 18 to 64 and NOT a student    → 800

    >>> ticket_price(10, False)
    300
    >>> ticket_price(22, True)
    500
    """
    pass


def format_greeting(name, age):
    """A5. Build a greeting with an f-string.

    - Remove any spaces around the name and make it Title Case.
    - Return exactly: "Hello <Name>, you are <age> years old."
    - If age is 1, use "year" instead of "years".

    >>> format_greeting("  amina ", 21)
    'Hello Amina, you are 21 years old.'
    >>> format_greeting("brian", 1)
    'Hello Brian, you are 1 year old.'
    """
    pass
