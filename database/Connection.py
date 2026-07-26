# database/connection.py

import mysql.connector
from mysql.connector import Error
import streamlit as st
from dotenv import load_dotenv
import os

# Reads the .env file and loads the variables into the environment
load_dotenv()

class DatabaseConnection:
    """
    Manages the MySQL database connection using the Singleton pattern.

    Only one connection instance exists for the entire application.
    All repositories use this class to get the connection.
    """

    # Shared across all calls — None means not connected yet
    _connection = None

    @classmethod
    def get_connection(cls):
        """
        Returns the active database connection.
        Creates a new one if it does not exist or was lost.

        Returns:
            mysql.connector connection object

        Raises:
            Exception: if the connection cannot be established
        """
        if cls._connection is None or not cls._connection.is_connected():
            try:
                cls._connection = mysql.connector.connect(
                    host     = os.getenv("DB_HOST"),
                    port     = int(os.getenv("DB_PORT")),
                    user     = os.getenv("DB_USER"),
                    password = os.getenv("DB_PASSWORD"),
                    database = os.getenv("DB_NAME")
                )

            except Error as e:
                raise Exception(f"Database connection failed: {e}")

        return cls._connection

    @classmethod
    def close_connection(cls):
        """
        Closes the connection if it is open.
        """
        if cls._connection is not None and cls._connection.is_connected():
            cls._connection.close()
            cls._connection = None
