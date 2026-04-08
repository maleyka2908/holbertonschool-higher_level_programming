#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to a MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to fetch all states, sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Retrieve all results from the executed query
    rows = cursor.fetchall()

    # Display results as required in the example
    for row in rows:
        print(row)

    # Clean up: close cursor and database connection
    cursor.close()
    db.close()
