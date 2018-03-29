#!usr/bin/env python3

import sqlite3


connection = sqlite3.connect('../run/datastore/master.db', check_same_thread=False)
cursor     = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password
    ) VALUES(
        'greg',
        'greg'
    );"""
)

connection.commit()
cursor.close()
connection.close()
