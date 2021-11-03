import os
import sqlite3


def tracks_count():
    db_path = os.path.join(os.getcwd(), 'example.db')
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    cursor.execute('''SELECT count() FROM tracks;''')
    res=(cursor.fetchone())

    db.commit()
    db.close()

    return res[0]


def unique_name():
    db_path = os.path.join(os.getcwd(), 'example.db')
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    cursor.execute('''SELECT count(DISTINCT FirstName) FROM customers;''')
    res=(cursor.fetchone())

    db.commit()
    db.close()

    return res[0]