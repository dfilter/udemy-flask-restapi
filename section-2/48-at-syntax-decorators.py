import functools

user = {'name': 'Jose', 'access_level': 'admin'}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'No Admin Permission for user {user["name"]}'
    
    return secure_function

@make_secure
def get_admin_password():
    return '1234'


print(get_admin_password())
