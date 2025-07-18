usernames = input().split(", ")
usernames = list(filter(lambda x: (3 <= len(x) <= 13 and x.replace("-", "").replace("_", "").isalnum()), usernames))
print("\n".join(usernames))