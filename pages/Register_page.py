# pages/register_page.py

import streamlit as st
from services.auth_services import AuthService

def show_register_page():
    """Renders the registration page."""

    st.title("Student Management System")
    st.subheader("Create an Account")

    auth_service = AuthService()

    with st.form("register_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm  = st.text_input("Confirm Password", type="password")
        submit   = st.form_submit_button("Register")

    if submit:
        if password != confirm:
            st.error("Passwords do not match.")
        else:
            success, message = auth_service.register(username, password)
            if success:
                st.success(message)
                st.info("Redirecting to login...")
                st.session_state["page"] = "login"
                st.rerun()
            else:
                st.error(message)

    st.divider()
    st.write("Already have an account?")
    if st.button("Back to Login"):
        st.session_state["page"] = "login"
        st.rerun()
