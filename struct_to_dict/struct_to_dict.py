"""
Structure to Dictionary Conversion
Converts structured data records / C-like struct representations to Python dictionaries.
Assignment: Python Programs Collection
"""

from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class StudentRecord:
    student_id: str
    name: str
    course: str
    semester: int
    cgpa: float


def struct_to_dict(record: StudentRecord) -> Dict[str, Any]:
    """Convert a structured student record into a clean Python dictionary."""
    return asdict(record)


def parse_c_struct_string_to_dict(c_struct_str: str) -> Dict[str, str]:
    """
    Parses a plain C struct definition string into a field-to-type dictionary.
    Useful for bridging C structures into Pythonic dictionaries.
    """
    fields = {}
    lines = c_struct_str.strip().splitlines()
    for line in lines:
        cleaned = line.strip().rstrip(";")
        if not cleaned or cleaned.startswith(("{", "}", "struct", "//")):
            continue
        parts = cleaned.split()
        if len(parts) >= 2:
            data_type = parts[0]
            field_name = parts[1]
            fields[field_name] = data_type
    return fields


if __name__ == "__main__":
    student = StudentRecord(
        student_id="25BCON0187",
        name="Yugank",
        course="Computer Science Engineering",
        semester=4,
        cgpa=9.1
    )
    student_dict = struct_to_dict(student)
    print("Converted Student Record to Dictionary:")
    for key, value in student_dict.items():
        print(f"  {key}: {value}")
