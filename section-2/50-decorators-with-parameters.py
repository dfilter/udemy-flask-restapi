import functools

user = {'name': 'Jose', 'access_level': 'admin'}


def make_secure(access_level):
    """ this is not a decorator it is what is called a "factory" - a 
    function that creates decorators. """
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            """ here we use args and kwargs to ensure that any number of 
            arguments can be passed along to the wrapped function. """
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f'No Admin Permission for user {user["name"]}'

        return secure_function

    return decorator


@make_secure('admin')
def get_admin_password():
    return 'admin: 1234'


@make_secure('user')
def get_dashboard_password():
    return 'user: 4321'


print(get_admin_password())
print(get_dashboard_password())
