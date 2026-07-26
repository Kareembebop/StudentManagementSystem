# database/student_repository.py

from database.Connection import DatabaseConnection
from models.Student import Student

class StudentRepository:
    """
    Handles all SQL operations for the students table.
    No business logic here — only database queries.
    """

    def __init__(self):
        self.conn = DatabaseConnection.get_connection()

    def get_all(self) -> list[Student]:
        """Returns all students from the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        cursor.close()
        return [Student(*row) for row in rows]

    def get_by_id(self, student_id: str) -> Student | None:
        """Returns a single student by ID, or None if not found."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM students WHERE student_id = %s",
            (student_id,)
        )
        row = cursor.fetchone()
        cursor.close()
        return Student(*row) if row else None

    def search(self, keyword: str) -> list[Student]:
        """Returns students whose name or ID contains the keyword."""
        cursor = self.conn.cursor()
        cursor.execute(
            """SELECT * FROM students
               WHERE student_id LIKE %s OR name LIKE %s""",
            (f"%{keyword}%", f"%{keyword}%")
        )
        rows = cursor.fetchall()
        cursor.close()
        return [Student(*row) for row in rows]

    def add(self, student: Student) -> None:
        """Inserts a new student into the database."""
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO students
               (student_id, name, age, department, gpa)
               VALUES (%s, %s, %s, %s, %s)""",
            (student.student_id, student.name,
             student.age, student.department, student.gpa)
        )
        self.conn.commit()
        cursor.close()

    def update(self, student: Student) -> None:
        """Updates an existing student's information."""
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE students
               SET name = %s, age = %s, department = %s, gpa = %s
               WHERE student_id = %s""",
            (student.name, student.age,
             student.department, student.gpa, student.student_id)
        )
        self.conn.commit()
        cursor.close()

    def delete(self, student_id: str) -> None:
        """Deletes a student by ID."""
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )
        self.conn.commit()
        cursor.close()

    def exists(self, student_id: str) -> bool:
        """Returns True if a student with the given ID already exists."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT 1 FROM students WHERE student_id = %s",
            (student_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    def get_highest_gpa(self) -> Student | None:
        """Returns the student with the highest GPA."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM students ORDER BY gpa DESC LIMIT 1"
        )
        row = cursor.fetchone()
        cursor.close()
        return Student(*row) if row else None

    def count_by_department(self) -> list[tuple]:
        """Returns a list of (department, count) tuples."""
        cursor = self.conn.cursor()
        cursor.execute(
            """SELECT department, COUNT(*) as total
               FROM students
               GROUP BY department
               ORDER BY total DESC"""
        )
        rows = cursor.fetchall()
        cursor.close()
        return rows
