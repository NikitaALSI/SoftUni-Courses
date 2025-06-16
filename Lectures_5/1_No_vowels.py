vowels = ['a', 'o', 'u', 'e', 'i']
string = input()
filtered_string = [char for char in string if char.lower() not in vowels]
print("".join(filtered_string))