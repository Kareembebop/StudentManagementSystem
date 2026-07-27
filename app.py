# app.py

import streamlit as st
from pages.login_page     import show_login_page
from pages.Register_page  import show_register_page
from pages.admin_dashboard import show_admin_dashboard
from pages.user_dashboard  import show_user_dashboard
from pages.chatbot_page   import show_chatbot_page

def initialize_session():
    """Sets default session state values on first load."""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "role" not in st.session_state:
        st.session_state["role"] = None
    if "username" not in st.session_state:
        st.session_state["username"] = None
    if "page" not in st.session_state:
        st.session_state["page"] = "login"

def main():
    """Main routing function."""

    st.set_page_config(
        page_title = "Student Management System",
        page_icon  = "🎓",
        layout     = "wide"
    )

    initialize_session()

    # ── Routing ───────────────────────────────────────────────
    if not st.session_state["logged_in"]:
        if st.session_state["page"] == "register":
            show_register_page()
        else:
            show_login_page()

    else:
        role = st.session_state["role"]
        page = st.session_state["page"]

        if role == "admin":
            show_admin_dashboard()

        elif role == "user":
            if page == "chatbot":
                show_chatbot_page()
            else:
                show_user_dashboard()

if __name__ == "__main__":
    main()
