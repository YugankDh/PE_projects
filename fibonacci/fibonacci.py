"""
Fibonacci Sequence Generator
Generates the Fibonacci sequence up to n terms.
Assignment: Python Programs Collection
"""

def generate_fibonacci(n_terms: int) -> list[int]:
    """Generate a list containing the first n terms of the Fibonacci sequence."""
    if not isinstance(n_terms, int) or n_terms < 0:
        raise ValueError("Number of terms must be a non-negative integer.")
    if n_terms == 0:
        return []
    if n_terms == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n_terms:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence


if __name__ == "__main__":
    count = 10
    print(f"First {count} terms of Fibonacci sequence:")
    print(generate_fibonacci(count))
