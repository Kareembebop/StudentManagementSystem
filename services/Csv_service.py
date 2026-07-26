# services/csv_service.py

import pandas as pd
from database.student_repository import StudentRepository
from models.Student import Student
from utils.Validator import Validator

class CSVService:
    """
    Handles CSV file import for bulk student uploads.

    Validates every row before inserting.
    Skips duplicate student IDs.
    Reports how many rows were added and which were invalid.
    """

    def __init__(self):
        self.repo      = StudentRepository()
        self.validator = Validator()

    def import_csv(self, file) -> dict:
        """
        Reads a CSV file and imports valid student rows.

        Expected CSV columns:
            student_id, name, age, department, gpa

        Returns a dict with:
            added    : number of students successfully added
            skipped  : number of duplicate IDs skipped
            invalid  : list of (row_number, reason) for bad rows
        """
        result = {
            "added":   0,
            "skipped": 0,
            "invalid": []
        }

        try:
            df = pd.read_csv(file)
        except Exception as e:
            result["invalid"].append((0, f"Could not read CSV file: {e}"))
            return result

        required_columns = {"student_id", "name", "age", "department", "gpa"}
        if not required_columns.issubset(df.columns):
            result["invalid"].append((0, "CSV must have columns: student_id, name, age, department, gpa"))
            return result

        for index, row in df.iterrows():
            row_num = index + 2  # row 1 is the header

            student_id = str(row.get("student_id", "")).strip()
            name       = str(row.get("name", "")).strip()
            age        = str(row.get("age", "")).strip()
            department = str(row.get("department", "")).strip()
            gpa        = str(row.get("gpa", "")).strip()

            # Validate the row
            is_valid, message = self.validator.validate_student(
                student_id, name, age, department, gpa
            )
            if not is_valid:
                result["invalid"].append((row_num, message))
                continue

            # Skip duplicates
            if self.repo.exists(student_id):
                result["skipped"] += 1
                continue

            # Insert the student
            student = Student(
                student_id = student_id,
                name       = name,
                age        = int(age),
                department = department,
                gpa        = float(gpa)
            )
            self.repo.add(student)
            result["added"] += 1

        return result
