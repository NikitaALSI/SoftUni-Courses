version = int("".join(input().split(".")))
new_version = [i for i in str(version + 1)]
print(".".join(new_version))