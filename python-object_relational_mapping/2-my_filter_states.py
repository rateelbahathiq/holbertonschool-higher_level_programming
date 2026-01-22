#!/usr/bin/python3
"""
Displays all values in the states table where the name
matches the argument provided.
"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    Connects to a MySQL database and displays states
    matching the given name.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(state_name)
    )
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
