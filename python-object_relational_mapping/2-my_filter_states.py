#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument provided.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    
    # Tapşırıq bizdən .format() istifadə etməyi tələb edir
    # Qeyd: Bu üsul SQL Injection-a qarşı zəifdir, lakin tapşırıq şərtidir.
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
             ORDER BY states.id ASC".format(sys.argv[4])
    
    cursor.execute(query)
    
    # Nəticələri çap etmək
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
        
    # Bağlantıları kəsmək
    cursor.close()
    db.close()
