# pages/login_page.py

import streamlit as st
from services.auth_services import AuthService

def show_login_page():
    """Renders the login page."""

    st.title("Student Management System")
    st.subheader("Login")

    auth_service = AuthService()

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit   = st.form_submit_button("Login")

    if submit:
        success, result = auth_service.login(username, password)

        if success:
            st.success(f"Welcome, {username}!")
            st.rerun()
        else:
            st.error(result)

    st.divider()
    st.write("Don't have an account?")
    if st.button("Register here"):
        st.session_state["page"] = "register"
        st.rerun()
