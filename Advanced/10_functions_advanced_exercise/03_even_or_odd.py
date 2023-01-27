def even_odd(*args):
    statement = 0 if args[-1] == 'even' else 1
    return [x for x in args[:-1] if x % 2 == statement]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
