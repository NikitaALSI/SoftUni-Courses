names = input().split(", ")
sort_by_len = sorted(names, key=lambda x: ("a" in x.lower(), -len(x)), reverse=True)
print(sort_by_len)