import sqlite3
from sqlite3 import Error

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite version:", sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return conn

# Function to create a new registration record
def create_registration(conn, registration):
    sql = ''' INSERT INTO Registration(Name, Email, DateOfBirth)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, registration)
    conn.commit()
    return cur.lastrowid

# Function to retrieve registration records
def retrieve_registration(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Registration")
    rows = cur.fetchall()
    return rows

# Function to update an existing registration record
def update_registration(conn, registration):
    sql = ''' UPDATE Registration
              SET Name = ? ,
                  Email = ? ,
                  DateOfBirth = ?
              WHERE ID = ?'''
    cur = conn.cursor()
    cur.execute(sql, registration)
    conn.commit()

# Function to delete a registration record
def delete_registration(conn, id):
    sql = 'DELETE FROM Registration WHERE ID=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

# Main function to demonstrate usage
def main():
    database = "registration.db"
    conn = create_connection(database)
    with conn:
        # Example usage of CRUD operations
        # Create a new registration
        registration_data = ('John Doe', 'john@example.com', '1990-01-01')
        registration_id = create_registration(conn, registration_data)
        print("New registration ID:", registration_id)

        # Retrieve all registrations
        registrations = retrieve_registration(conn)
        print("\nAll registrations:")
        for row in registrations:
            print(row)

        # Update a registration
        update_data = ('Jane Doe', 'jane@example.com', '1995-05-05', registration_id)
        update_registration(conn, update_data)
        print("\nRegistration updated.")

        # Retrieve all registrations after update
        updated_registrations = retrieve_registration(conn)
        print("\nAll registrations after update:")
        for row in updated_registrations:
            print(row)

        # Delete a registration
        delete_registration(conn, registration_id)
        print("\nRegistration deleted.")

        # Retrieve all registrations after deletion
        remaining_registrations = retrieve_registration(conn)
        print("\nAll registrations after deletion:")
        for row in remaining_registrations:
            print(row)

if __name__ == '__main__':
    main()
