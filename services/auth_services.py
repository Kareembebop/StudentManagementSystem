# services/auth_service.py

import streamlit as st
from database.admin_repository import AdminRepository
from database.user_repository import UserRepository
from models.User import User

class AuthService:
    """
    Handles all authentication logic.

    Responsibilities:
    - Login for both admins and users
    - Registration for normal users
    - Session management via Streamlit session state
    - Role checking
    """

    def __init__(self):
        self.admin_repo = AdminRepository()
        self.user_repo  = UserRepository()

    def login(self, username: str, password: str) -> tuple[bool, str]:
        """
        Attempts to log in as admin first, then as user.

        Returns:
            (True, role)  if login succeeded
            (False, message) if login failed
        """
        if not username or not password:
            return False, "Username and password cannot be empty."

        # Check admin table first
        admin = self.admin_repo.get_by_username(username)
        if admin and admin.password == password:
            st.session_state["logged_in"] = True
            st.session_state["username"]  = admin.username
            st.session_state["role"]      = "admin"
            return True, "admin"

        # Check users table
        user = self.user_repo.get_by_username(username)
        if user and user.password == password:
            st.session_state["logged_in"] = True
            st.session_state["username"]  = user.username
            st.session_state["role"]      = "user"
            return True, "user"

        return False, "Invalid username or password."

    def register(self, username: str, password: str) -> tuple[bool, str]:
        """
        Registers a new normal user.

        Returns:
            (True, success message) or (False, error message)
        """
        if not username or not password:
            return False, "Username and password cannot be empty."

        if len(username) < 3:
            return False, "Username must be at least 3 characters."

        if len(password) < 6:
            return False, "Password must be at least 6 characters."

        if self.user_repo.exists(username):
            return False, "Username already taken. Please choose another."

        new_user = User(username=username, password=password)
        self.user_repo.add(new_user)
        return True, "Registration successful. You can now log in."

    def logout(self) -> None:
        """Clears the session state to log the user out."""
        st.session_state["logged_in"] = False
        st.session_state["username"]  = None
        st.session_state["role"]      = None

    def is_logged_in(self) -> bool:
        """Returns True if a user is currently logged in."""
        return st.session_state.get("logged_in", False)

    def get_role(self) -> str | None:
        """Returns the current user's role or None."""
        return st.session_state.get("role", None)

    def get_username(self) -> str | None:
        """Returns the current user's username or None."""
        return st.session_state.get("username", None)
