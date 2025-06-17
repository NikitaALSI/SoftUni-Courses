def add(title, some_schedule):
    if title not in some_schedule:
        some_schedule.append(title)
    return some_schedule


def insert(title, index, some_schedule):
    if title not in some_schedule:
        some_schedule.insert(int(index), title)
    return some_schedule


def remove(title, some_schedule):
    if title in some_schedule:
        some_schedule.remove(title)
    if f"{title}-Exercise" in some_schedule:
        some_schedule.remove(f"{title}-Exercise")
    return some_schedule


def swap(title1, title2, some_schedule):
    copy_list = some_schedule[:]
    if title1 and title2 in some_schedule:
        some_schedule[some_schedule.index(title1)] = title2
        some_schedule[copy_list.index(title2)] = title1
        if f"{title1}-Exercise" in some_schedule:
            some_schedule.remove(f"{title1}-Exercise")
            some_schedule.insert(some_schedule.index(title1) + 1, f"{title1}-Exercise")
        if f"{title2}-Exercise" in some_schedule:
            some_schedule.remove(f"{title2}-Exercise")
            some_schedule.insert(some_schedule.index(title2) + 1, f"{title2}-Exercise")
    return some_schedule


def exercise(title, some_schedule):
    if title in some_schedule and f"{title}-Exercise" not in some_schedule:
        some_schedule.insert(some_schedule.index(title)+1, f"{title}-Exercise")
    elif title not in some_schedule and f"{title}-Exercise" not in some_schedule:
        addition = [title, f"{title}-Exercise"]
        some_schedule.extend(addition)
    return some_schedule


schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    elif "Add" in command:
        action, lesson_title = command.split(":")
        schedule = add(lesson_title, schedule)
    elif "Insert" in command:
        action, lesson_title, lesson_index = command.split(":")
        schedule = insert(lesson_title, lesson_index, schedule)
    elif "Remove" in command:
        action, lesson_title = command.split(":")
        schedule = remove(lesson_title, schedule)
    elif "Swap" in command:
        action, lesson_title1, lesson_title2 = command.split(":")
        schedule = swap(lesson_title1, lesson_title2, schedule)
    elif "Exercise" in command:
        action, lesson_title = command.split(":")
        schedule = exercise(lesson_title, schedule)


for i, lesson in enumerate(schedule):
    print(f"{i+1}.{lesson}")
