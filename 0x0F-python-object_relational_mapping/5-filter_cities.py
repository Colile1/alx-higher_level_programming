#!/usr/bin/python3
"""
 takes in the name of a state as an argument
 and lists all cities of that state
"""
import sys
import MySQLdb


if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])

    cur = connection.cursor()
    state_name = sys.argv[4]
    cur.execute("""
            SELECT cities.name
            FROM cities INNER JOIN states ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY states.id ASC
            """, (state_name,))

    rows = cur.fetchall()
    elements = list(element[0] for element in rows)
    print(*elements, sep=", ")
    cur.close()
    connection.close()
