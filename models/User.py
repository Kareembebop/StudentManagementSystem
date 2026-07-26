# models/user.py

class User:
    """
    Represents a normal (non-admin) user account.

    Base class for authentication entities.
    Admin inherits from this class.

    Attributes:
        user_id  : Integer ID from the database (0 if not saved yet)
        username : Unique login name
        password : Plain text password
        role     : Always "user" for this class
    """

    def __init__(
        self,
        username: str,
        password: str,
        user_id: int = 0
    ) -> None:
        self.user_id  = user_id
        self.username = username
        self.password = password
        self.role     = "user"

    def __repr__(self) -> str:
        return (
            f"User(id={self.user_id}, "
            f"username={self.username!r}, "
            f"role={self.role!r})"
        )
