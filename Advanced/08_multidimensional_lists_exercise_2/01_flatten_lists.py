initial_list = input().split("|")

flatten_list = []

for sub_string in initial_list[::-1]:
    flatten_list.extend(sub_string.split())

print(*flatten_list)
