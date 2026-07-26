# test_repositories.py

from database.student_repository import StudentRepository
from database.user_repository import UserRepository
from database.admin_repository import AdminRepository

# Test StudentRepository
student_repo = StudentRepository()
students = student_repo.get_all()
print(f"Total students: {len(students)}")
print("First student:", students[0])

# Test get_highest_gpa
top = student_repo.get_highest_gpa()
print("Highest GPA:", top)

# Test count by department
dept_counts = student_repo.count_by_department()
print("Department counts:", dept_counts)

# Test AdminRepository
admin_repo = AdminRepository()
admin = admin_repo.get_by_username("admin")
print("Admin found:", admin)

# Test UserRepository
user_repo = UserRepository()
print("User exists (should be False):", user_repo.exists("someone"))
