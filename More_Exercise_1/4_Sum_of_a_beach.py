beach_string = input().lower()

if 'sand' in beach_string:
    count += beach_string.count('sand')
if 'water' in beach_string.lower():
    count += beach_string.count('water')
if 'fish' in beach_string.lower():
    count += beach_string.count('fish')
if 'sun' in beach_string.lower():
    count += beach_string.count('sun')

print(count)
