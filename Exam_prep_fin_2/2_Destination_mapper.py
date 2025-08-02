import re

places = input()
place_pat = r'([=\/])([A-Z][A-Za-z]{2,})(\1)'
valid_places_iter = re.finditer(place_pat, places)
valid_places_names = [x.group(2) for x in valid_places_iter]
travel_points = sum([len(x) for x in valid_places_names])
print(f"Destinations: {', '.join(valid_places_names)}")
print(f"Travel Points: {travel_points}")
