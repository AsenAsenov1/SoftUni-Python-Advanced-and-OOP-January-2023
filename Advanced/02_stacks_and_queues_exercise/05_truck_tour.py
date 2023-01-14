from collections import deque

pumps_count = int(input())
pumps = deque()

for _ in range(pumps_count):
    pumps.append([int(x) for x in input().split()])

for attempt in range(pumps_count):
    tank_level = 0
    for petrol, distance in pumps:
        tank_level += petrol - distance
        if tank_level < 0:
            pumps.rotate(-1)
            break
    else:
        print(attempt)
        break
