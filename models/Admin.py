# models/admin.py

from models.User import User

class Admin(User):
    """
    Represents an admin account.

    Inherits username and password behaviour from User.
    Overrides role to "admin".
    Uses admin_id to match the admins table in the database.

    Attributes:
        admin_id : Integer ID from the admins table (0 if not saved yet)
        username : Unique login name
        password : Plain text password
        role     : Always "admin"
    """

    def __init__(
        self,
        username: str,
        password: str,
        admin_id: int = 0
    ) -> None:
        # Call User's constructor to set username and password
        super().__init__(username=username, password=password)

        self.admin_id = admin_id
        self.role     = "admin"   # override the "user" role set by parent

    def __repr__(self) -> str:
        return (
            f"Admin(id={self.admin_id}, "
            f"username={self.username!r}, "
            f"role={self.role!r})"
        )
