import re

participants = {name: 0 for name in input().split(", ")}
pat_name = r'[a-z]'
pat_km = r'\d'

while (code := input()) != "end of race":
    name = "".join(re.findall(pat_name, code, re.I))
    km = sum(map(int, re.findall(pat_km, code)))
    if name in participants:
        participants[name] += km

rank_list = list(dict(sorted(participants.items(), key=lambda x: x[1], reverse=True)).keys())
print(f"1st place: {rank_list[0]}")
print(f"2nd place: {rank_list[1]}")
print(f"3rd place: {rank_list[2]}")