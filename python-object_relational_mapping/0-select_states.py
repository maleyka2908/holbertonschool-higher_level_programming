#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
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

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute SQL query to select all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    query_rows = cursor.fetchall()

    # Display the results
    for row in query_rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
