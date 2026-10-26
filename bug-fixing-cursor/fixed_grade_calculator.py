"""
Fixed Grade Calculator
All 3 defects corrected following the RED -> FIX -> GREEN methodology (Assignment 8).
"""

def calculate_average(scores: list[float]) -> float:
    """Calculates true average based on dynamic length of scores list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def is_passing(score: float, pass_mark: float = 40.0) -> bool:
    """Evaluates passing status with inclusive boundary condition."""
    return score >= pass_mark


def determine_letter_grade(percentage: float) -> str:
    """Evaluates letter grade using properly ordered descending thresholds."""
    if percentage >= 90.0:
        return "A"
    elif percentage >= 75.0:
        return "B"
    elif percentage >= 50.0:
        return "C"
    elif percentage >= 40.0:
        return "D"
    else:
        return "F"
