users = [
    (0, 'Bob', 'password'),
    (1, 'Rolf', 'bob123'),
    (2, 'Jose', 'longp4assword'),
    (3, 'username', '1234')
]

# Assigning key to value in tuple at index 1 aka "Bob", "Rolf" etc.
username_mapping = {user[1]: user for user in users}
print(username_mapping)
