number = float(input())

output = "zero"

if 0 < abs(number) < 1:
    output = "small "
elif 1 <= abs(number) <= 1000000:
    output = ""
elif abs(number) > 1000000:
    output = "large "

if number > 0:
    output += "positive"
elif number < 0:
    output += "negative"

print(output)
