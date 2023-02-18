"""
On the first line, you will be given a sequence representing textiles. On the second line, you will be given another
sequence, which represents medicaments.
While both collections contain any elements, you will have to combine elements from the collections in order to create
healing items. You should start by getting the first value of textile and the last value of medicaments:
•	If their sum is equal to any of the items in the table below create that item and remove both values.
•	Otherwise, check if the sum is bigger than the value of the MedKit, create the MedKit, remove both values, and add
the remaining resources(of the sum) to the next value in the medicament collection (Take the element from the collection,
add the remaining sum to it, and put the element back to its place).
•	If you can’t create anything, remove the textile value, add 10 to the medicament value, and return the medicament
back to its place, into its collection.
You need to stop creating healing items when either the textile or the medicaments are exhausted.
Healing item	Resources needed
Patch	30
Bandage	40
MedKit	100

In the end, you should print on the console message for the sequence that has ended, then the created items, and in the
end the remaining items (if any).
"""

from collections import deque

textiles = deque([int(x) for x in input().split()])
meds = [int(x) for x in input().split()]

supplies = {"Patch": 0,
            "Bandage": 0,
            "MedKit": 0}
items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}

while textiles and meds:
    current_txt = textiles.popleft()
    current_med = meds.pop()
    sum_supplies = current_txt + current_med

    if sum_supplies == items["Patch"]:
        supplies['Patch'] += 1
    elif sum_supplies == items["Bandage"]:
        supplies['Bandage'] += 1
    elif sum_supplies == items["MedKit"]:
        supplies['MedKit'] += 1
    elif sum_supplies > items["MedKit"]:
        supplies['MedKit'] += 1
        remaining_resources = sum_supplies - items["MedKit"]
        meds[-1] += remaining_resources
    else:
        current_med += 10
        meds.append(current_med)
sorted_supp = sorted(supplies.items(), key=lambda x: (-x[1], x[0]))

if len(textiles) == 0 and len(meds) == 0:
    print("Textiles and medicaments are both empty.")
elif len(meds) == 0:
    print("Medicaments are empty.")
elif len(textiles) == 0:
    print("Textiles are empty.")

for element in sorted_supp:
    if int(element[1]) > 0:
        print(f"{element[0]} - {element[1]}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
if meds:
    print(f"Medicaments left: {', '.join(map(str, meds[::-1]))}")
