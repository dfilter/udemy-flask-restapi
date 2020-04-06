# "*args" collects all the passed arguments into one tuple variable
# called "args"
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(1, 3, 5))


def add(x, y):
    return x + y


nums = [3, 5]
# Unpack the above list using "*" ensure that there are the same
# number of elements as there are arguments for the function.
print(add(*nums))

nums = {'x': 15, 'y': 25}
print(add(x=nums['x'], y=nums['y']))

# Same as above but unpack the dictionary key value pairs as arguments
print(add(**nums))


def apply(*args, operator):
    if operator == '*':
        # Unpack the tuple and pass to multiply
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return 'No valid operator provided to apply().'


print(apply(1, 3, 6, 7, operator='+'))
