pair = input().split()
first = [x for x in pair[0]]
second = [x for x in pair[1]]
code = 0
for _ in range(min(len(first), len(second))):
    code += ord(first.pop(0)) * ord(second.pop(0))
for char in first:
    code += ord(char)
for char in second:
    code += ord(char)

print(code)
