import mysql.connector
from tkinter import messagebox
from config import DB_CONFIG

def get_db_connection():
    """Create and return database connection"""
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            autocommit=False
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", "Failed to connect: " + str(err))
        return None