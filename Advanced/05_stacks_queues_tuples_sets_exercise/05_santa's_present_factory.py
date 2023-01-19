from collections import deque

materials_stack = [int(x) for x in input().split()]
magic_values_deque = deque(int(x) for x in input().split())
task_done = False

presents_info = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
collected_presents = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while materials_stack and magic_values_deque:
    material_value_peek = materials_stack[-1]
    magic_value_peek = magic_values_deque[0]

    result = material_value_peek * magic_value_peek

    if result in presents_info.keys():
        toy = presents_info[result]
        collected_presents[toy] += 1
        materials_stack.pop()
        magic_values_deque.popleft()
    else:
        if magic_value_peek == 0 and material_value_peek == 0:
            materials_stack.pop()
            magic_values_deque.popleft()
            continue
        elif material_value_peek == 0:
            materials_stack.pop()
            continue
        elif magic_value_peek == 0:
            magic_values_deque.popleft()
            continue

        if result not in presents_info.keys() and result > 0:
            magic_values_deque.popleft()
            materials_stack.append(materials_stack.pop() + 15)
        elif result < 0:
            values_sum = material_value_peek + magic_value_peek
            materials_stack.pop()
            magic_values_deque.popleft()
            materials_stack.append(values_sum)

materials_left = [str(materials_stack.pop()) for _ in range(len(materials_stack))]

if collected_presents["Doll"] and collected_presents["Wooden train"] > 0 or \
        collected_presents["Teddy bear"] and collected_presents["Bicycle"] > 0:
    task_done = True

if task_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_left:
    print(f"Materials left: {', '.join(materials_left)}")

if magic_values_deque:
    print(f"Magic left: {', '.join(str(x) for x in magic_values_deque)}")

for toy, count in sorted(collected_presents.items()):
    if count > 0:
        print(f"{toy}: {count}")
