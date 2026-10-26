"""
Refactored Student Performance Script
Refactored using AI-assisted clean code principles (Experiment 6).
Output matches original output character-for-character, with clean structure and reusable functions.
"""

MAX_POSSIBLE_SCORE = 100

student_1_scores = [85, 92, 78, 64, 89]
student_2_scores = [70, 75, 80, 85, 90]
student_3_scores = [55, 60, 58, 62, 65]


def calculate_average(scores: list[float]) -> float:
    """Calculate the arithmetic mean for a sequence of numeric scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def count_students_above_average(student_averages: list[float], class_average: float) -> int:
    """Counts how many students scored strictly above the overall class average."""
    return sum(1 for avg in student_averages if avg > class_average)


def main() -> None:
    avg_student_1 = calculate_average(student_1_scores)
    avg_student_2 = calculate_average(student_2_scores)
    avg_student_3 = calculate_average(student_3_scores)

    all_scores = student_1_scores + student_2_scores + student_3_scores
    overall_batch_avg = calculate_average(all_scores)

    # Output matches the original character-for-character using modern f-strings
    print(f"Student 1 Avg: {round(avg_student_1, 2)} / {MAX_POSSIBLE_SCORE}")
    print(f"Student 2 Avg: {round(avg_student_2, 2)} / {MAX_POSSIBLE_SCORE}")
    print(f"Student 3 Avg: {round(avg_student_3, 2)} / {MAX_POSSIBLE_SCORE}")
    print(f"Overall Batch Avg: {round(overall_batch_avg, 2)} / {MAX_POSSIBLE_SCORE}")


if __name__ == "__main__":
    main()
