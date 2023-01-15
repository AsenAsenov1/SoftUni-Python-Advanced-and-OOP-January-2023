guests_invited = int(input())

reservations = set([input() for person in range(guests_invited)])
people_attended = set()

while True:
    attendant = input()
    if attendant == "END":
        break
    people_attended.add(attendant)

not_attended = reservations.difference(people_attended)
not_attended_sorted = list(sorted(not_attended))

print(len(not_attended))
print("\n".join(not_attended_sorted))
