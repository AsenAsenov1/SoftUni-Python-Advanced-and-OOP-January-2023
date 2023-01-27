def even_odd_filter(**kwargs):
    filtered_lists = {}
    for key, value in kwargs.items():
        if key == "odd":
            filtered_lists[key] = [num for num in value if num % 2 != 0]
        elif key == "even":
            filtered_lists[key] = [num for num in value if num % 2 == 0]
    return {k: v for k, v in sorted(filtered_lists.items(), key=lambda item: -len(item[1]))}


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

# Output:
# {'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}
