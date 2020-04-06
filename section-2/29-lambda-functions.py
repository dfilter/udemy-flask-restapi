def add(x, y):
    return x + y


# Same as above function
add = lambda x, y: x + y

print(add(1, 2))

# lambda function can be executed without being named like this:
sum_ = (lambda x, y: x + y)(5, 7)
print(sum_)


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]

# same as above but using "map()" function. 
# Note that map is slower then list comprehension
# Note that map returns a map object and not a list
doubled = list(map(double, sequence))

# to do the same as above but with a lambda expression:
# Note that the bottom one is preferred as it is more readable
doubled = [(lambda x: x * 2)(x) for x in sequence)]
doubled = list(map(lambda x: x * 2, sequence))
