#!/usr/bin/python3
"""
    Lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = connection.cursor()
    cur.execute("""
                SELECT * FROM states
                WHERE name LIKE BINARY 'N%' ORDER BY id ASC
                """)
    rows = cur.fetchall()
    for element in rows:
        print(element)
    cur.close()
    connection.close()
