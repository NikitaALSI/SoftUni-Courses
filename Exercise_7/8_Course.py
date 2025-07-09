courses = {}

while (cmd := input()) != "end":
    course, student = cmd.split(" : ")
    courses[course] = courses.get(course, []) + [student]
else:
    for course in courses:
        print(f"{course}: {len(courses[course])}")
        for student in courses[course]:
            print(f"-- {student}")
