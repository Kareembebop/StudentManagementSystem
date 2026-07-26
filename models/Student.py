# models/student.py

class Student:
    """
    Represents a single student record.

    This is a pure data model — it holds student information
    and nothing else. No database code, no business logic.

    Attributes:
        student_id  : Formatted string ID, e.g. "S001"
        name        : Full name of the student
        age         : Age as an integer
        department  : Department name
        gpa         : Grade Point Average (0.00 to 4.00)
    """

    def __init__(
            self,
            student_id: str,
            name: str,
            age: int,
            department: str,
            gpa: float
        ) -> None:
        self.student_id  = student_id
        self.name        = name
        self.age         = age
        self.department  = department
        self.gpa         = gpa

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation.
        Useful when printing or debugging a Student object.
        """
        return (
            f"Student(id={self.student_id!r}, "
            f"name={self.name!r}, "
            f"age={self.age}, "
            f"department={self.department!r}, "
            f"gpa={self.gpa})"
        )
