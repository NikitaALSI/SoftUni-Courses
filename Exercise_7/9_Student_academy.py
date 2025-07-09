students = int(input())
grades = {}

for _ in range(students):
    student = input()
    grade = float(input())
    grades[student] = grades.get(student, []) + [grade]

for student in grades:
    average = sum(grades[student]) / len(grades[student])
    if average >= 4.5:
        print(f"{student} -> {average:.2f}")

