import sqlite3
from settings import database

# Saves input to the database.


def save(sql, params):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(sql, params)
    conn.commit()
    conn.close()
