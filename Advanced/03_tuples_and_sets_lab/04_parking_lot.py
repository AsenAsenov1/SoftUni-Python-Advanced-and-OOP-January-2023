registry_number = int(input())

parking = []

for _ in range(registry_number):
    operation, car = input().split(", ")
    if operation == "IN":
        parking.append(car)
    elif operation == "OUT":
        if car in parking:
            parking.remove(car)

if parking:
    print("\n".join(set(parking)))
else:
    print("Parking Lot is Empty")
