# Collects all the passed keyword arguments and adds them to a dictionary
def named(**kwargs):
    print(kwargs)


named(name='Bob', age=25)


def named(name, age):
    print(name, age)


details = {'name': 'Bob', 'age': 25}
# Unpack dictionary and pass as keyword arguments
named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    # Unpack kwargs dictionary into keys and values
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')


print_nicely(name='Bob', age=25)

# collect all arguments into args tuple and keyword arguments into 
# kwargs dictionary
def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 3, name='Bob', age=25)
