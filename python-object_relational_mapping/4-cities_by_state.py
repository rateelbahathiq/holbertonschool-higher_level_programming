#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
along with their corresponding state names.
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Connects to a MySQL database and lists all cities
    ordered by cities.id in ascending order.
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
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
