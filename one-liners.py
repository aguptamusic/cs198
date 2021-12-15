
### One - Liners ###

## Points: return a list with sums of x/y coordinates.
points = [(1, 2), (4, 4), (1, 3)]
"""
-> yields [3, 8, 4]
"""
# With list comprehension:
sum = [pt[0] + pt[1] for pt in points]
print("List of coordinate sums:")
print(sum)

# Equivalently, With map() and a lambda function:
sum = map(lambda pt: pt[0] + pt[1], points)
print(list(sum))

# ------------------------ #

## Cities:
cities = [('modesto', 95351, 92), ('palo alto', 94301, 80), ('sacramento', 94203, 100)]

# Call sorted() to produce a list of these tuples sorted in decreasing
# order by temperature.
sorted_cities = sorted(cities, key=lambda city: city[2], reverse=True)
print(sorted_cities)
    