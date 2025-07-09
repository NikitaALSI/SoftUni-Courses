phonebook = {}
while "-" in (contact := input()):
    name, phone = contact.split("-")
    phonebook[name] = phone

for _ in range(int(contact)):
    name = input()
    if not phonebook.get(name):
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")