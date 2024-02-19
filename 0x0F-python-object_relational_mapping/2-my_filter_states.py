#!/usr/bin/python3

"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db_connect = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3],
    )

    db_cursor = db_connect.cursor()


    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
        .format(argv[4]))

    rows = db_cursor.fetchall()

    for row in rows:
        print(row)

    db_cursor.close()
    db_connect.close()
