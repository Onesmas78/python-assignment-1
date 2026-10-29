"""
Part C — Putting it together with functions (Classes 1 + 2)

Replace each `pass` with your code. Every function must RETURN its answer.
You may call your own functions from Part A — get_grade is already imported.

Check your work any time with:   pytest tests/test_part_c.py
"""

from part_a_basics import get_grade


def average(numbers):
    """C1. Return the average of the list, rounded to 2 decimal places.

    Return 0.0 if the list is empty (don't divide by zero!).

    >>> average([70, 80, 95])
    81.67
    >>> average([])
    0.0
    """
    pass


def class_report(marks):
    """C2. Given a dictionary of {name: mark}, return a NEW dictionary of
    {name: grade}, using your get_grade function from Part A.

    >>> class_report({"Amina": 74, "Brian": 58})
    {'Amina': 'A', 'Brian': 'C'}
    """
    pass


def top_student(marks):
    """C3. Given a dictionary of {name: mark}, return the NAME of the
    student with the highest mark.

    - If two students tie, return the one that appears first.
    - Return None if the dictionary is empty.

    >>> top_student({"Amina": 74, "Chen": 91, "Dee": 39})
    'Chen'
    """
    pass


def shopping_total(cart, prices, discount=0):
    """C4. Work out the total cost of a shopping cart in KES.

    - `cart` is a dict of {item: quantity}, e.g. {"bread": 2, "milk": 1}
    - `prices` is a dict of {item: price}, e.g. {"bread": 65, "milk": 60}
    - Skip any item in the cart that is not in `prices`.
    - `discount` is a percentage (default 0). Take it off the total.
    - Return the total rounded to 2 decimal places.

    >>> shopping_total({"bread": 2, "milk": 1}, {"bread": 65, "milk": 60})
    190
    >>> shopping_total({"bread": 2}, {"bread": 65}, discount=10)
    117.0
    """
    pass


def password_strength(password):
    """C5. Rate a password as "weak", "medium" or "strong".

    Count how many of these 3 rules it meets:
      1. At least 8 characters long
      2. Contains at least one digit         (hint: char.isdigit())
      3. Contains at least one uppercase letter (hint: char.isupper())

    3 rules → "strong",  2 rules → "medium",  0 or 1 rule → "weak"

    >>> password_strength("Nairobi2026")
    'strong'
    >>> password_strength("nairobi2026")
    'medium'
    >>> password_strength("abc")
    'weak'
    """
    pass
