#!/usr/bin/python3
"""
Displays all values in the states table where the name
matches the argument, safely (SQL injection protected).
"""

import MySQLdb
import sys


def safe_filter_states(username, password, database, state_name):
    """
    Connects to a MySQL database and safely displays states
    matching the given name using parameterized queries.
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
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (state_name,)
    )
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
