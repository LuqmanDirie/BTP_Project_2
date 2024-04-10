import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database specified by the docker-compose service name"""
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

def create_restaurant(owner_username, restaurant_name, address, phone, email):
    """Add a new restaurant to the Restaurants table"""
    conn = create_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Restaurants (owner_username, restaurant_name, address, phone, email)
            VALUES (%s, %s, %s, %s, %s)
        """, (owner_username, restaurant_name, address, phone, email))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error creating new restaurant: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_restaurant_by_id(restaurant_id):
    """Retrieve a restaurant by its ID"""
    conn = create_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Restaurants WHERE restaurant_id = %s", (restaurant_id,))
        return cursor.fetchone()
    except Error as e:
        print(f"Error fetching restaurant by ID: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def update_restaurant(restaurant_id, owner_username, restaurant_name, address, phone, email):
    """Update a restaurant record in the Restaurants table"""
    conn = create_connection()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Restaurants
            SET owner_username = %s, restaurant_name = %s, address = %s, phone = %s, email = %s
            WHERE restaurant_id = %s
        """, (owner_username, restaurant_name, address, phone, email, restaurant_id))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error updating restaurant: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def delete_restaurant(restaurant_id):
    """Delete a restaurant record from the Restaurants table"""
    conn = create_connection()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Restaurants WHERE restaurant_id = %s", (restaurant_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error deleting restaurant: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
