# test_services.py

from services.student_service import StudentService
from services.Chatbot_services import ChatbotService

# Test StudentService
student_service = StudentService()
students = student_service.get_all_students()
print(f"Total students: {len(students)}")

# Test add
success, message = student_service.add_student(
    "S009", "Test Student", "21", "Biology", "3.50"
)
print("Add:", message)

# Test duplicate
success, message = student_service.add_student(
    "S009", "Test Student", "21", "Biology", "3.50"
)
print("Duplicate:", message)

# Test delete
success, message = student_service.delete_student("S009")
print("Delete:", message)

# Test ChatbotService
chatbot = ChatbotService()
query_type, data = chatbot.respond("show all students")
print("Chatbot query type:", query_type)
print("Chatbot data count:", len(data))

query_type, data = chatbot.respond("something random")
print("Unknown query type:", query_type)
