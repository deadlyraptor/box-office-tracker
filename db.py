import sqlite3

# Saves input to the database.


def save(sql, params):
    conn = sqlite3.connect('/home/javier/Programming Projects/box-office-tracker/database/box_office_tracker.db')
    c = conn.cursor()
    c.execute(sql, params)
    conn.commit()
    conn.close()
