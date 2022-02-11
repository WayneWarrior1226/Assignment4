# This program will use list comprehension

first = [ x**2 for x in [x**2 for x in range(19)]]
print(first)
