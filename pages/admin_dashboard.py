# pages/admin_dashboard.py

import streamlit as st
import pandas as pd
from services.student_service import StudentService
from services.auth_services import AuthService
from services.Csv_service import CSVService

def show_admin_dashboard():
    """Renders the admin dashboard with full CRUD operations."""

    auth_service    = AuthService()
    student_service = StudentService()
    csv_service     = CSVService()

    # ── Sidebar ──────────────────────────────────────────────
    st.sidebar.title("Admin Panel")
    st.sidebar.write(f"Logged in as: **{auth_service.get_username()}**")

    if st.sidebar.button("Logout"):
        auth_service.logout()
        st.rerun()

    page = st.sidebar.radio(
        "Navigate",
        ["View Students", "Add Student", "Update Student",
         "Delete Student", "Search Student", "Upload CSV"]
    )

    st.title("Admin Dashboard")

    # ── View Students ─────────────────────────────────────────
    if page == "View Students":
        st.subheader("All Students")
        students = student_service.get_all_students()

        if not students:
            st.info("No students found.")
        else:
            data = [{
                "ID":         s.student_id,
                "Name":       s.name,
                "Age":        s.age,
                "Department": s.department,
                "GPA":        s.gpa
            } for s in students]
            st.dataframe(pd.DataFrame(data), use_container_width=True)
            st.caption(f"Total students: {len(students)}")

    # ── Add Student ───────────────────────────────────────────
    elif page == "Add Student":
        st.subheader("Add New Student")

        with st.form("add_form"):
            student_id = st.text_input("Student ID (e.g. S009)")
            name       = st.text_input("Full Name")
            age        = st.text_input("Age")
            department = st.text_input("Department")
            gpa        = st.text_input("GPA (0.00 - 4.00)")
            submit     = st.form_submit_button("Add Student")

        if submit:
            success, message = student_service.add_student(
                student_id, name, age, department, gpa
            )
            if success:
                st.success(message)
            else:
                st.error(message)

    # ── Update Student ────────────────────────────────────────
    elif page == "Update Student":
        st.subheader("Update Student")

        student_id = st.text_input("Enter Student ID to update")

        if student_id:
            student = student_service.get_student_by_id(student_id)

            if not student:
                st.error(f"No student found with ID '{student_id}'.")
            else:
                with st.form("update_form"):
                    name       = st.text_input("Full Name",   value=student.name)
                    age        = st.text_input("Age",         value=str(student.age))
                    department = st.text_input("Department",  value=student.department)
                    gpa        = st.text_input("GPA",         value=str(student.gpa))
                    submit     = st.form_submit_button("Update Student")

                if submit:
                    success, message = student_service.update_student(
                        student_id, name, age, department, gpa
                    )
                    if success:
                        st.success(message)
                    else:
                        st.error(message)

    # ── Delete Student ────────────────────────────────────────
    elif page == "Delete Student":
        st.subheader("Delete Student")

        with st.form("delete_form"):
            student_id = st.text_input("Enter Student ID to delete")
            submit     = st.form_submit_button("Delete Student")

        if submit:
            success, message = student_service.delete_student(student_id)
            if success:
                st.success(message)
            else:
                st.error(message)

    # ── Search Student ────────────────────────────────────────
    elif page == "Search Student":
        st.subheader("Search Students")

        keyword = st.text_input("Search by name or student ID")

        if keyword:
            results = student_service.search_students(keyword)

            if not results:
                st.warning("No students found.")
            else:
                data = [{
                    "ID":         s.student_id,
                    "Name":       s.name,
                    "Age":        s.age,
                    "Department": s.department,
                    "GPA":        s.gpa
                } for s in results]
                st.dataframe(pd.DataFrame(data), use_container_width=True)

    # ── Upload CSV ────────────────────────────────────────────
    elif page == "Upload CSV":
        st.subheader("Bulk Upload Students via CSV")

        st.info(
            "CSV file must have these columns: "
            "student_id, name, age, department, gpa"
        )

        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

        if uploaded_file:
            if st.button("Import"):
                result = csv_service.import_csv(uploaded_file)

                st.success(f"Successfully added: {result['added']} students")

                if result["skipped"] > 0:
                    st.warning(f"Skipped {result['skipped']} duplicate IDs")

                if result["invalid"]:
                    st.error(f"Invalid rows: {len(result['invalid'])}")
                    for row_num, reason in result["invalid"]:
                        st.write(f"Row {row_num}: {reason}")
