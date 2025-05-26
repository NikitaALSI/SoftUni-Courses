prime = True
number = int(input())

for i in range(2, number):
    if number % i == 0:
        prime = False

print(prime)