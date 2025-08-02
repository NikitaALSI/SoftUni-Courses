import re


places = input()

valid_places_pat = r"(=|\/)([A-Z][A-Za-z]{2,})(\1)"
valid_places = [x.group(2) for x in re.finditer(valid_places_pat, places)]
travel_points = sum(list(map(lambda x: len(x), valid_places)))
print(f"Destinations: {', '.join(valid_places)}\nTravel Points: {travel_points}")
