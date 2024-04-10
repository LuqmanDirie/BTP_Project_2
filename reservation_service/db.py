import mysql.connector
from mysql.connector import Error
import datetime

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

def create_reservation(diner_username, restaurant_name, reservation_time, number_of_people, status):
    """Create a new reservation in the Reservations table"""
    conn = create_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Reservations (diner_username, restaurant_name, reservation_time, number_of_people, status)
            VALUES (%s, %s, %s, %s, %s)
            """, (diner_username, restaurant_name, reservation_time, number_of_people, status))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error creating new reservation: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_reservation_by_id(reservation_id):
    """Fetch a single reservation by ID"""
    conn = create_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Reservations WHERE reservation_id = %s", (reservation_id,))
        reservation = cursor.fetchone()
        return reservation
    except Error as e:
        print(f"Error fetching reservation by ID: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_reservation(reservation_id, diner_username, restaurant_name, reservation_time, number_of_people, status):
    """Update an existing reservation in the Reservations table"""
    conn = create_connection()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Reservations
            SET diner_username = %s, restaurant_name = %s, reservation_time = %s, number_of_people = %s, status = %s
            WHERE reservation_id = %s
            """, (diner_username, restaurant_name, reservation_time, number_of_people, status, reservation_id))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error updating reservation: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def delete_reservation(reservation_id):
    """Delete a reservation from the Reservations table"""
    conn = create_connection()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Reservations WHERE reservation_id = %s", (reservation_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error deleting reservation: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
