"""
Buggy Grade Calculator
Contains 3 deliberate defects as studied in Assignment 8:
1. Average calculation bug (dividing by constant or incorrect index)
2. Passing boundary bug (fails on exactly 40/50 passing score because of > instead of >=)
3. Grade ordering bug (checks 'B' before 'A' or reversed ranges leading to wrong classification)
"""

def calculate_average(scores: list[float]) -> float:
    # BUG 1: Hardcoded divisor causing inaccurate average when list size differs
    total = sum(scores)
    return total / 5  # Bug if len(scores) != 5


def is_passing(score: float, pass_mark: float = 40.0) -> bool:
    # BUG 2: Uses strictly greater than instead of greater than or equal to
    return score > pass_mark  # Exactly 40.0 is erroneously marked failing!


def determine_letter_grade(percentage: float) -> str:
    # BUG 3: Incorrect conditional ordering evaluates B and C prematurely
    if percentage >= 75.0:
        return "B"  # Erroneous: scores 90+ incorrectly assigned 'B' instead of 'A'!
    elif percentage >= 90.0:
        return "A"
    elif percentage >= 50.0:
        return "C"
    elif percentage >= 40.0:
        return "D"
    else:
        return "F"
