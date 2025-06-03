n = int(input())
word = input()
strings = [input() for _ in range(n)]
print(strings)
filtered_sting = [string for string in strings if word in string]
print(filtered_sting)
