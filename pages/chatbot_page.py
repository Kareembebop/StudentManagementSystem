# pages/chatbot_page.py

import streamlit as st
import pandas as pd
from services.Chatbot_services import ChatbotService
from services.auth_services import AuthService

def show_chatbot_page():
    """Renders the rule-based chatbot interface."""

    auth_service    = AuthService()
    chatbot_service = ChatbotService()

    # ── Sidebar ───────────────────────────────────────────────
    st.sidebar.title("User Panel")
    st.sidebar.write(f"Logged in as: **{auth_service.get_username()}**")

    if st.sidebar.button("Logout"):
        auth_service.logout()
        st.rerun()

    if st.sidebar.button("Back to Dashboard"):
        st.session_state["page"] = "user_dashboard"
        st.rerun()

    # ── Chatbot UI ────────────────────────────────────────────
    st.title("Student Database Chatbot")

    st.info("""
    **Suggested Questions:**
    1. Show all students
    2. Show the student with the highest GPA
    3. Count students in each department

    Type one of the questions exactly.
    """)

    with st.form("chatbot_form"):
        user_input = st.text_input("Your question:")
        submit     = st.form_submit_button("Send")

    if submit and user_input:
        query_type, data = chatbot_service.respond(user_input)

        if query_type == "all":
            st.subheader("All Students")
            rows = [{
                "ID":         s.student_id,
                "Name":       s.name,
                "Age":        s.age,
                "Department": s.department,
                "GPA":        s.gpa
            } for s in data]
            st.dataframe(pd.DataFrame(rows), use_container_width=True)

        elif query_type == "highest":
            if data:
                st.subheader("Student with Highest GPA")
                st.write(f"**Name:** {data.name}")
                st.write(f"**ID:** {data.student_id}")
                st.write(f"**Department:** {data.department}")
                st.write(f"**GPA:** {data.gpa}")
            else:
                st.warning("No students found.")

        elif query_type == "count":
            st.subheader("Students per Department")
            rows = [{"Department": dept, "Count": count}
                    for dept, count in data]
            st.dataframe(pd.DataFrame(rows), use_container_width=True)

        else:
            st.warning("""
            I'm just a dummy chatbot 🤖

            I only know these three predefined questions.
            Please choose one of the suggested questions.
            """)
