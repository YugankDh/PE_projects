"""
Factorial Program
Calculates the factorial of a non-negative integer using recursion and iteration.
Assignment: C to Python Conversion & Python Programs Collection
"""

def factorial_recursive(n: int) -> int:
    """Calculate factorial of n using recursion."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Calculate factorial of n using iteration."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    test_val = 5
    print(f"Calculating factorial for n = {test_val}:")
    print(f"Recursive: {test_val}! = {factorial_recursive(test_val)}")
    print(f"Iterative: {test_val}! = {factorial_iterative(test_val)}")
