country_capitals = {country: capital for country, capital in zip(input().split(", "), input().split(", "))}
for country, capital in country_capitals.items():
    print(f"{country} -> {capital}")