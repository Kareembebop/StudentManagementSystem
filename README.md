# 🎓 Student Management System

A full-stack web application built with **Python**, **Streamlit**, and **MySQL**.
Designed using clean Object-Oriented Programming principles and a professional 4-layer architecture.

---

## 📸 Overview

This system supports two types of users — **Admins** and **Normal Users** — each with their own dashboard and set of features.

---

## ✨ Features

### 🔐 Admin
- Secure login with role-based access
- Add, update, delete, and search student records
- View all students in an interactive table
- Bulk import students from a CSV file with row-by-row validation

### 👤 Normal User
- Register and log in
- Access a rule-based chatbot to query the student database

### 🤖 Chatbot
A simple rule-based chatbot that responds to exactly **3 predefined questions**:
- `Show all students`
- `Show the student with the highest GPA`
- `Count students in each department`

> No AI, no NLP — just clean, deterministic logic.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Core language |
| Streamlit | Web UI |
| MySQL (XAMPP) | Database |
| mysql-connector-python | Database driver |
| pandas | Data handling and CSV processing |
| python-dotenv | Environment variable management |

---

## 🏗️ Architecture

```
Streamlit UI  →  Service Layer  →  Repository Layer  →  MySQL Database
```

| Layer | Responsibility |
|-------|---------------|
| UI (pages/) | Renders the interface, handles user input |
| Service (services/) | Contains all business logic and validation |
| Repository (database/) | Contains all SQL queries |
| Models (models/) | Pure data classes, no logic |

> The UI never executes SQL. Repositories never contain business logic. Every class has a single responsibility.

---

## 🧱 OOP Concepts Applied

| Concept | Where |
|---------|-------|
| **Encapsulation** | Models hold only their own data |
| **Inheritance** | `Admin` inherits from `User` |
| **Abstraction** | Services hide all repository complexity from the UI |
| **Composition** | Services contain repositories as dependencies |

---

## 📁 Project Structure

```
StudentManagementSystem/
│
├── app.py                        ← Entry point and page router
│
├── models/
│   ├── student.py                ← Student data model
│   ├── user.py                   ← User base class
│   └── admin.py                  ← Admin (inherits User)
│
├── database/
│   ├── connection.py             ← Singleton database connection
│   ├── student_repository.py     ← Student SQL queries
│   ├── user_repository.py        ← User SQL queries
│   └── admin_repository.py       ← Admin SQL queries
│
├── services/
│   ├── auth_service.py           ← Login, register, logout, session
│   ├── student_service.py        ← Student business logic
│   ├── csv_service.py            ← CSV import logic
│   └── chatbot_service.py        ← Rule-based chatbot
│
├── pages/
│   ├── login_page.py             ← Login UI
│   ├── register_page.py          ← Registration UI
│   ├── admin_dashboard.py        ← Admin dashboard
│   ├── user_dashboard.py         ← User dashboard
│   └── chatbot_page.py           ← Chatbot UI
│
├── utils/
│   └── validator.py              ← Input validation rules
│
├── .env                          ← Database credentials (not committed)
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.10+
- XAMPP with MySQL running
- Git

### 2. Clone the Repository
```bash
git clone https://github.com/Kareembebop/StudentManagementSystem.git
cd StudentManagementSystem
```

### 3. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the project root:
```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=StudentDB
```

### 6. Set Up the Database
Start XAMPP and open `http://localhost/phpmyadmin`.

Run the following SQL:

```sql
CREATE DATABASE IF NOT EXISTS StudentDB;
USE StudentDB;

CREATE TABLE admins (
    admin_id  INT          AUTO_INCREMENT PRIMARY KEY,
    username  VARCHAR(50)  NOT NULL UNIQUE,
    password  VARCHAR(100) NOT NULL
);

CREATE TABLE users (
    user_id   INT          AUTO_INCREMENT PRIMARY KEY,
    username  VARCHAR(50)  NOT NULL UNIQUE,
    password  VARCHAR(100) NOT NULL
);

CREATE TABLE students (
    student_id  VARCHAR(20)  NOT NULL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    age         INT          NOT NULL,
    department  VARCHAR(100) NOT NULL,
    gpa         DECIMAL(3,2) NOT NULL
);

INSERT INTO admins (username, password) VALUES ('admin', 'admin123');
```

### 7. Run the Application
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🔑 Default Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| User | register a new account | — |

---

## 📋 CSV Import Format

To bulk import students, upload a CSV file with these exact columns:

```
student_id,name,age,department,gpa
S009,John Smith,21,Biology,3.50
S010,Sara Lee,22,Physics,3.75
```

The system will:
- ✅ Add valid rows
- ⚠️ Skip duplicate student IDs
- ❌ Report invalid rows with reasons

---

## ✅ Validation Rules

| Field | Rule |
|-------|------|
| Student ID | Cannot be empty, must be unique |
| Name | Cannot be empty, cannot contain numbers |
| Age | Integer between 15 and 100 |
| Department | Cannot be empty |
| GPA | Decimal between 0.00 and 4.00 |
| Username | Minimum 3 characters, must be unique |
| Password | Minimum 6 characters |

---

## 👨‍💻 Author

Built as a portfolio project demonstrating Python OOP, clean architecture, and full-stack development with Streamlit and MySQL.
