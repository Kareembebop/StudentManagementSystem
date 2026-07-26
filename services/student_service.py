# services/student_service.py

from database.student_repository import StudentRepository
from models.Student import Student
from utils.Validator import Validator

class StudentService:
    """
    Handles all business logic for student operations.

    Uses StudentRepository for database access.
    Uses Validator to enforce data rules before any DB operation.
    """

    def __init__(self):
        self.repo      = StudentRepository()
        self.validator = Validator()

    def get_all_students(self) -> list[Student]:
        """Returns all students."""
        return self.repo.get_all()

    def search_students(self, keyword: str) -> list[Student]:
        """Returns students matching the keyword."""
        if not keyword:
            return self.repo.get_all()
        return self.repo.search(keyword)

    def get_student_by_id(self, student_id: str) -> Student | None:
        """Returns a single student by ID."""
        return self.repo.get_by_id(student_id)

    def add_student(
        self,
        student_id: str,
        name: str,
        age: str,
        department: str,
        gpa: str
    ) -> tuple[bool, str]:
        """
        Validates and adds a new student.

        Returns:
            (True, success message) or (False, error message)
        """
        is_valid, message = self.validator.validate_student(
            student_id, name, age, department, gpa
        )
        if not is_valid:
            return False, message

        if self.repo.exists(student_id):
            return False, f"Student ID '{student_id}' already exists."

        student = Student(
            student_id  = student_id,
            name        = name,
            age         = int(age),
            department  = department,
            gpa         = float(gpa)
        )
        self.repo.add(student)
        return True, f"Student '{name}' added successfully."

    def update_student(
        self,
        student_id: str,
        name: str,
        age: str,
        department: str,
        gpa: str
    ) -> tuple[bool, str]:
        """
        Validates and updates an existing student.

        Returns:
            (True, success message) or (False, error message)
        """
        if not self.repo.exists(student_id):
            return False, f"Student ID '{student_id}' not found."

        is_valid, message = self.validator.validate_student(
            student_id, name, age, department, gpa
        )
        if not is_valid:
            return False, message

        student = Student(
            student_id  = student_id,
            name        = name,
            age         = int(age),
            department  = department,
            gpa         = float(gpa)
        )
        self.repo.update(student)
        return True, f"Student '{student_id}' updated successfully."

    def delete_student(self, student_id: str) -> tuple[bool, str]:
        """
        Deletes a student by ID.

        Returns:
            (True, success message) or (False, error message)
        """
        if not self.repo.exists(student_id):
            return False, f"Student ID '{student_id}' not found."

        self.repo.delete(student_id)
        return True, f"Student '{student_id}' deleted successfully."
