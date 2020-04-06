friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}

# "difference()" checks the abroad set and remove items that are not in friends and returns the result
local_friends = friends.difference(abroad)
print(local_friends)

local = {'Rolf'}
abroad = {'Bob', 'Anne'}

# "union()" adds the set from abroad to the local set and returns the result
friends = local.union(abroad)
print(friends)

art = {'Bob', 'Jen', 'Rolf', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

# "intersection()" finds what items are in both sets and returns that result
both = art.intersection(science)
