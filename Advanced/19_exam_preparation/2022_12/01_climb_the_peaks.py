from collections import deque

daily_food = list(map(int, input().split(", ")))
daily_stamina = deque(map(int, input().split(", ")))

day = 1
conquered_peaks = []
all_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

while True:
    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if day > 7 or not daily_food or not daily_stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
    food = daily_food.pop()
    stamina = daily_stamina.popleft()
    result = food + stamina
    index = 0
    next_peak = all_peaks.popleft()
    if result >= next_peak[1]:
        conquered_peaks.append(next_peak[0])
        day += 1
    else:
        all_peaks.appendleft(next_peak)
        day += 1


if conquered_peaks:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)
