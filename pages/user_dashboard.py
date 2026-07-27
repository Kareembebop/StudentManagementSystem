# pages/user_dashboard.py

import streamlit as st
from services.auth_services import AuthService

def show_user_dashboard():
    """Renders the normal user dashboard."""

    auth_service = AuthService()

    # ── Sidebar ───────────────────────────────────────────────
    st.sidebar.title("User Panel")
    st.sidebar.write(f"Logged in as: **{auth_service.get_username()}**")

    if st.sidebar.button("Logout"):
        auth_service.logout()
        st.rerun()

    # ── Main Content ──────────────────────────────────────────
    st.title("Welcome!")
    st.write(f"Hello, **{auth_service.get_username()}**.")
    st.write("Use the chatbot to query the student database.")

    if st.button("Open Chatbot"):
        st.session_state["page"] = "chatbot"
        st.rerun()
