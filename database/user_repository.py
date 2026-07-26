# database/user_repository.py

from database.Connection import DatabaseConnection
from models.User import User

class UserRepository:
    """
    Handles all SQL operations for the users table.
    """

    def __init__(self):
        self.conn = DatabaseConnection.get_connection()

    def get_by_username(self, username: str) -> User | None:
        """Returns a user by username, or None if not found."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT user_id, username, password FROM users WHERE username = %s",
            (username,)
        )
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(username=row[1], password=row[2], user_id=row[0])
        return None

    def add(self, user: User) -> None:
        """Inserts a new user into the database."""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (user.username, user.password)
        )
        self.conn.commit()
        cursor.close()

    def exists(self, username: str) -> bool:
        """Returns True if a username is already taken."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT 1 FROM users WHERE username = %s",
            (username,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result is not None
