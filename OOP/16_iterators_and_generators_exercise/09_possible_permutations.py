from itertools import permutations


def possible_permutations(integers_list: list):
    result = permutations(integers_list)
    for permutation in result:
        yield list(permutation)
