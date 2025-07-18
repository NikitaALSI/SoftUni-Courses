import re
lines = int(input())
for _ in range(lines):
    text = input()
    # pat_name = r'(?<=@)(.+)(?=\|)'
    pat_name = r'@(.+)\|'
    # pat_age = r'(?<=#)(.+)(?=\*)'
    pat_age = r'#(.+)\*'
    name = re.findall(pat_name, text)
    age = re.findall(pat_age, text)
    print(f"{name} is {age} years old.")