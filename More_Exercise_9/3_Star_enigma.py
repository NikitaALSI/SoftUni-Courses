import re

attacked = []
destroyed = []
n = int(input())
for _ in range(n):
    encrypted = input()
    key = len(re.findall(r'[star]', encrypted, re.I))
    decrypted = "".join(list(map(lambda x: chr(ord(x) - key), [x for x in encrypted])))
    planet_pat = r'[^@\-!:>]*@([A-Za-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-!:>]*->(\d+)[^@\-!:>]*'
    found = re.match(planet_pat, decrypted)
    if found:
        planet, population, attack_type, soldier_count = found.groups()
        if attack_type == "A":
            attacked.append(planet)
        elif attack_type == "D":
            destroyed.append(planet)

print(f"Attacked planets: {len(attacked)}")
for planet in list(sorted(attacked)):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed)}")
for planet in list(sorted(destroyed)):
    print(f"-> {planet}")

