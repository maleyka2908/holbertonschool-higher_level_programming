#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
The script takes 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if correct number of arguments are provided (optional but good)
    if len(sys.argv) < 4:
        exit()

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()
