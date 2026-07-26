# services/chatbot_service.py

from database.student_repository import StudentRepository

class ChatbotService:
    """
    A simple rule-based chatbot.

    Recognizes exactly three predefined questions.
    Returns a fallback message for anything else.
    No AI, no NLP, no machine learning.
    """

    QUERY_ALL        = "show all students"
    QUERY_HIGHEST    = "show the student with the highest gpa"
    QUERY_COUNT_DEPT = "count students in each department"

    def __init__(self):
        self.repo = StudentRepository()

    def respond(self, user_input: str) -> tuple[str, any]:
        """
        Compares input against the three supported queries.

        Returns:
            (query_type, data)
            query_type is one of: "all", "highest", "count", "unknown"
            data is the query result or None
        """
        normalized = user_input.strip().lower()

        if normalized == self.QUERY_ALL:
            students = self.repo.get_all()
            return "all", students

        elif normalized == self.QUERY_HIGHEST:
            student = self.repo.get_highest_gpa()
            return "highest", student

        elif normalized == self.QUERY_COUNT_DEPT:
            counts = self.repo.count_by_department()
            return "count", counts

        else:
            return "unknown", None
