import mysql.connector
from mysql.connector import Error
import hashlib
from datetime import datetime

def create_connection():
    """Create a database connection"""
    try:
        connection = mysql.connector.connect(
            host='RRS-db',
            user='root',
            password='RRSpassword',
            database='restaurant_db',
            port=3306
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

def update_user(user_id, username, email, password, user_type):
    """Update an existing user in the Users table"""
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    conn = create_connection()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Users SET username = %s, email = %s, password_hash = %s, user_type = %s WHERE user_id = %s",
            (username, email, hashed_password, user_type, user_id)
        )
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error updating user: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def delete_user(user_id):
    """Delete a user from the Users table"""
    conn = create_connection()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error deleting user: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def create_user(username, email, password, user_type):
    """Create a new user in the Users table"""
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    conn = create_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Users (username, email, password_hash, user_type) VALUES (%s, %s, %s, %s)",
            (username, email, hashed_password, user_type)
        )
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error creating new user: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_user_by_id(user_id):
    conn = create_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM Users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        if user and 'creation_date' in user and user['creation_date']:
            # Convert TIMESTAMP to string
            user['creation_date'] = user['creation_date'].strftime('%Y-%m-%dT%H:%M:%S')
        return user
    except Error as e:
        print(f"Error fetching user by ID: {e}")
        return None
    finally:
        if conn:
            conn.close()