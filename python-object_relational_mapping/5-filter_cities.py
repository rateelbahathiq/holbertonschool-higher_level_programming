#!/usr/bin/python3
"""
Lists all cities of a given state from the database
hbtn_0e_4_usa, safely from SQL injection.
"""

import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """
    Connects to a MySQL database and prints all cities
    of the given state, ordered by cities.id.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id ASC
        """,
        (state_name,)
    )

    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
