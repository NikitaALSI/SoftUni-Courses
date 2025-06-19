pirating_days = int(input())
plunder_for_day = int(input())
expected_plunder = int(input())
total_gain = 0

for day in range(1, pirating_days+1):
    total_gain += plunder_for_day
    if day % 3 == 0:
        total_gain += 0.5 * plunder_for_day
    if day % 5 == 0:
        total_gain *= (1 - 0.3)

if total_gain >= expected_plunder:
    print(f"Ahoy! {total_gain:.2f} plunder gained.")
else:
    print(f"Collected only {(total_gain / expected_plunder)*100:.2f}% of the plunder.")