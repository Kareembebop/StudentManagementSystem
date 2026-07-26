# utils/validator.py

class Validator:
    """
    Validates student and user input data.
    All methods return (is_valid: bool, message: str).
    """

    def validate_student(
        self,
        student_id: str,
        name: str,
        age: str,
        department: str,
        gpa: str
    ) -> tuple[bool, str]:
        """Validates all student fields."""

        if not student_id or not student_id.strip():
            return False, "Student ID cannot be empty."

        if not name or not name.strip():
            return False, "Name cannot be empty."

        if any(char.isdigit() for char in name):
            return False, "Name cannot contain numbers."

        try:
            age_int = int(age)
        except ValueError:
            return False, "Age must be a whole number."

        if age_int < 15 or age_int > 100:
            return False, "Age must be between 15 and 100."

        if not department or not department.strip():
            return False, "Department cannot be empty."

        try:
            gpa_float = float(gpa)
        except ValueError:
            return False, "GPA must be a number."

        if gpa_float < 0.0 or gpa_float > 4.0:
            return False, "GPA must be between 0.00 and 4.00."

        return True, "Valid"
