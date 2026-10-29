"""
Part B — Lists, dictionaries and loops (Class 2)

Replace each `pass` with your code. Every function must RETURN its answer.
Use loops — some exercises ask you NOT to use a shortcut built-in.

Check your work any time with:   pytest tests/test_part_b.py
"""


def sum_of_evens(numbers):
    """B1. Return the sum of only the even numbers in the list.

    Return 0 if there are none.

    >>> sum_of_evens([1, 2, 3, 4, 10])
    16
    >>> sum_of_evens([])
    0
    """
    pass


def largest(numbers):
    """B2. Return the largest number in the list WITHOUT using max().

    Return None if the list is empty.

    >>> largest([3, 9, 2])
    9
    >>> largest([-5, -2, -8])
    -2
    >>> largest([]) is None
    True
    """
    pass


def reverse_words(sentence):
    """B3. Return the sentence with the order of the words reversed.

    Hint: .split() and " ".join(...)

    >>> reverse_words("python is fun")
    'fun is python'
    """
    pass


def word_count(text):
    """B4. Return a dictionary of how many times each word appears.

    - Treat words as lowercase ("The" and "the" are the same word).
    - Split on spaces only; you do not need to remove punctuation.

    >>> word_count("the cat and the hat")
    {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
    """
    pass


def remove_duplicates(items):
    """B5. Return a NEW list with duplicates removed, keeping the
    first occurrence of each item in its original order.

    >>> remove_duplicates([3, 1, 3, 2, 1])
    [3, 1, 2]
    >>> remove_duplicates(["a", "b", "a"])
    ['a', 'b']
    """
    pass
