numbers = [int(input()) for _ in range(int(input()))]

positive = [number for number in numbers if number >= 0]
negative = [number for number in numbers if number < 0]

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")


