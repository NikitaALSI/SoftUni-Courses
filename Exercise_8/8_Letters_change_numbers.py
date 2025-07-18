blocks = input().split()
total_sum = 0
for block in blocks:
    number = int(block[1:-1])
    if block[0].isupper():
        number /= (ord(block[0]) - (ord("A")-1))
    else:
        number *= (ord(block[0]) - (ord("a")-1))

    if block[-1].isupper():
        number -= (ord(block[-1]) - (ord("A")-1))
    else:
        number += (ord(block[-1]) - (ord("a")-1))
    total_sum += number
print(f"{total_sum:.2f}")
