number_of_students = int(input())
students_grades = {}

for _ in range(number_of_students):
    student, grade = input().split()
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for student, grade in students_grades.items():
    avg = sum(grade) / len(grade)
    grade_str = " ".join(list(map(lambda x: f"{x:.2f}", grade)))
    print(f"{student} -> {grade_str} (avg: {avg:.2f})")
