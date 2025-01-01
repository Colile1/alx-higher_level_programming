#!/usr/bin/python3
""" safe from MySQL injections! """
import sys
import MySQLdb


if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = connection.cursor()
    state_name = sys.argv[4]
    cur.execute("""SELECT * FROM states
                    WHERE name= %s ORDER BY id ASC""", (state_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    connection.close()
