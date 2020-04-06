numbers = [1, 3, 5]
doubled = []

for number in numbers:
    doubled.append(number * 2)

# Same as above
doubled = [number * 2 for number in numbers]
print(doubled)

friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
starts_s = []

for friend in friends:
    if friend.startswith('S'):
        starts_s.append(friend)

# same as above loop
starts_s = [friend for friend in friends if friend.startswith('S')]
print(starts_s)
