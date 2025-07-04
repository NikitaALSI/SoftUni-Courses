courses = {}

while True:
    cmd = input().split(":")
    if len(cmd) == 1:
        break

    name, ID, course = cmd
    courses[course] = courses.get(course, []) + [f"{name} - {int(ID)}"]

for student in courses[cmd[0].replace("_", " ")]:
    print(student)
