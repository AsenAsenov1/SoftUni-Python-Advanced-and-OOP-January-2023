clothes_box = list(map(int, input().split()))
rack_capacity = int(input())
racks_counter = 1
current_rack = 0

while clothes_box:
    current_cloth = clothes_box.pop()

    if current_cloth + current_rack <= rack_capacity:
        current_rack += current_cloth
    else:
        current_rack = current_cloth
        racks_counter += 1

print(racks_counter)
