# test_connection.py

from database.Connection import DatabaseConnection

try:
    conn = DatabaseConnection.get_connection()
    print("Connection successful!")
    print("Connected to:", conn.database)

    conn2 = DatabaseConnection.get_connection()
    print("Same connection object?", conn is conn2)

except Exception as e:
    print("Error:", e)
