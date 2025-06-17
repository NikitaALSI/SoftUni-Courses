rooms = int(input())
total_free_chairs = 0
enough = True
for room in range(1, rooms + 1):
    chairs, visitors = input().split()
    if len(chairs) < int(visitors):
        needed_chairs_in_room = int(visitors) - len(chairs)
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")
        enough = False
    else:
        total_free_chairs += len(chairs) - int(visitors)

if enough:
    print(f"Game On, {total_free_chairs} free chairs left")
