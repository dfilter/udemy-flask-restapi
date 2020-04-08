import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
database_location = os.path.join(dir_path, 'data.db')

connection = sqlite3.connect(database_location)
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

connection.commit()
connection.close()
