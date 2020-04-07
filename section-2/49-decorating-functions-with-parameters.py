import functools

user = {'name': 'Jose', 'access_level': 'admin'}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        """ here we use args and kwargs to ensure that any number of 
        arguments can be passed along to the wrapped function. """
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f'No Admin Permission for user {user["name"]}'
    
    return secure_function

@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return '4321'


print(get_password('billing'))
