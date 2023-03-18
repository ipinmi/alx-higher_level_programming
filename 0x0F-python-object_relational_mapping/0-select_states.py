#!/usr/bin/python3
#
#
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
