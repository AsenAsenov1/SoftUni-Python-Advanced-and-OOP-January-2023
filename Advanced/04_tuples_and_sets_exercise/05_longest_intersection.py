number = int(input())

largest_set = {}

for _ in range(number):
    ranges_1, ranges_2 = input().split("-")
    start1, stop1 = ranges_1.split(",")
    start2, stop2 = ranges_2.split(",")
    set1 = {x for x in range(int(start1), int(stop1) + 1)}
    set2 = {x for x in range(int(start2), int(stop2) + 1)}
    intersect_set = set1.intersection(set2)
    if len(intersect_set) > len(largest_set):
        largest_set = intersect_set

print(f"Longest intersection is {list(largest_set)} with length {len(largest_set)}")
