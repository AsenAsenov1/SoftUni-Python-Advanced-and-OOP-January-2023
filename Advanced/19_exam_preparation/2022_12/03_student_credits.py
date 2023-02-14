"""
Write a function students_credits which receives a different number of strings.
Each string will be in the format: "{course name}-{credits}-{max test points}-{diyan's points}".
Your task is to calculate the credits Diyan manages to get from all courses. The credits he gets are proportional to
his points on the test. For example, if the credits of a course are 25, and Diyan achieved to get 50 of 100 max test points,
he will get 12.5 credits for the course.
Also, you need to keep track of each course and Diyan's credits and sort them in descending order by Diyan's credits.
Finally, return a string on multiple lines containing:
•	Diyan's achievement message:
o	If the sum of all of Diyan's credits is more than or equal to 240, return: "Diyan gets a diploma with {total credits} credits."
o	Otherwise, return: "Diyan needs {credits needed} credits more for a diploma."
•	Information for each course and Diyan's credits:
o	"{course name} - {diyan's credits}"
o	Note: Each course data should be on a new line.
•	All credits must be formatted to the first decimal place.

Eample Output

Diyan gets a diploma with 243.3 credits.
Game Engine Development - 49.0
Algorithms Advanced - 45.0
Discrete Maths - 36.0
C++ Development - 24.3
Mobile Development - 22.5
AI Development - 20.0
QA - 20.0
Python Development - 15.0
JavaScript Development - 11.5
"""


def students_credits(*args):
    score_dict = {}
    total_credits = 0
    print_text = []

    for data in args:
        data = data.split("-")
        course_name = data[0]
        credits_num, max_test_points, diyan_points = [int(x) for x in data[1:]]

        try:
            result = credits_num / (max_test_points / diyan_points)
        except ZeroDivisionError:
            result = 0

        total_credits += result
        score_dict[course_name] = result

    if total_credits >= 240:
        print_text.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        print_text.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")

    print_text.extend(f"{course} - {pts:.1f}" for course, pts in sorted(score_dict.items(), key=lambda x: -float(x[1])))

    return "\n".join(print_text)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
