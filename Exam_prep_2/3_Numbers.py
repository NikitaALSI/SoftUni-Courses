sequence = list(map(int, input().split()))
greate_than_the_average = sorted(list(filter(lambda x: x > (sum(sequence) / len(sequence)), sequence)),reverse=True)
if greate_than_the_average:
    print(" ".join(list(map(str, greate_than_the_average[:5]))))
else:
    print("No")