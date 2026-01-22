#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
that start with the letter 'N'.
"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Connects to a MySQL database and lists all states
    whose names start with 'N', ordered by id.
    """
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
