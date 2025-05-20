sheep_string = input()
sheep_list = []
message = ''
word = ''
for char in sheep_string:

    if char == ' ':
        word = ''
        continue
    if char == ',':
        sheep_list.append(word)
    word += char

sheep_list.append(word)
sheep_list = sheep_list[::-1]

if sheep_list[0] == 'wolf':
    message = 'Please go away and stop eating my sheep'
else:
    for position, entity in enumerate(sheep_list):
        if entity == 'wolf':
            message = f'Oi! Sheep number {position}! You are about to be eaten by a wolf!'

print(message)