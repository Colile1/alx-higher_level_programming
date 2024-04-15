#!/usr/bin/python3
"""
    Prints every value in the states table of
    hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb


if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = connection.cursor()
    state_name = sys.argv[4]
    cur.execute("""SELECT * FROM states
                    WHERE name LIKE BINARY '{}'
                    ORDER BY id ASC
                """ .format(state_name))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    connection.close()
