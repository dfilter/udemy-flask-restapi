import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
database_location = os.path.join(dir_path, 'data.db')

connection = sqlite3.connect(database_location)
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'dirk', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'rolf', 'asdf'),
    (2, 'anne', 'asdf')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
