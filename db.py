import sqlite3
from settings import database

# Saves input to the database.


def connect_db():
    return sqlite3.connect(database)


def save(sql, params):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(sql, params)
    conn.commit()
    conn.close()

"""
def unsettled():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('select count(settled) from films where settled = 0;')
    conn.commit()
    conn.close()
"""
