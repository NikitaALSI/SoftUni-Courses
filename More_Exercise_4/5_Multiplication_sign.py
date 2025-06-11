def multiplication_sign(a, b, c):
    text =str(a)+str(b)+str(c)
    if a == "0" or b == "0" or c == "0":
        return "zero"
    if text.count("-") % 2 == 0:
        return "positive"
    return "negative"


print(multiplication_sign(input(), input(), input()))