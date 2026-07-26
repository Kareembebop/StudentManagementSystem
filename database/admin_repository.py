# database/admin_repository.py

from database.Connection import DatabaseConnection
from models.Admin import Admin

class AdminRepository:
    """
    Handles all SQL operations for the admins table.
    """

    def __init__(self):
        self.conn = DatabaseConnection.get_connection()

    def get_by_username(self, username: str) -> Admin | None:
        """Returns an admin by username, or None if not found."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT admin_id, username, password FROM admins WHERE username = %s",
            (username,)
        )
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Admin(username=row[1], password=row[2], admin_id=row[0])
        return None

    def exists(self, username: str) -> bool:
        """Returns True if an admin username already exists."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT 1 FROM admins WHERE username = %s",
            (username,)
        )
        result = cursor.fetchone()
        cursor.close()
        return result is not None
