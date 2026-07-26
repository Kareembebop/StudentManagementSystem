# test_models.py

from models.Student import Student
from models.User import User
from models.Admin import Admin

s = Student("S001", "Alice Johnson", 20, "Computer Science", 3.85)
u = User("john_doe", "pass123")
a = Admin("admin", "admin123")

print(s)
print(u)
print(a)
print("Is Admin a User?", isinstance(a, User))
