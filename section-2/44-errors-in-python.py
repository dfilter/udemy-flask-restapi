def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')

    return dividend / divisor


grades = [78, 99, 85, 100]

print('Welcome to the average grade program.')
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print('There are no grades yet in your list.')
else:
    # if no error happened run this code:
    print(f'The average grade is {average}.')

students = [{
    'name': 'Bob',
    'grades': [75, 90]
}, {
    'name': 'Rolf',
    'grades': []
}, {
    'name': 'Jen',
    'grades': [100, 90]
}]

try:
    for student in stundents:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades), len(grades))
        print(f'{name} averaged {average}.')
except ZeroDivisionError:
    print(f'ERROR: {name} has no grades.')
else:
    print("-- All student's average calculated. --")
finally:
    print("-- Finished calculating student's averages --")
