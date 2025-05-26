# def happy_year(year):
#     while True:
#         year += 1
#         year_digits = ''
#         for digit in str(year):
#             if digit not in year_digits:
#                 year_digits += digit
#             else:
#                 break
#         else:
#             yield year
#
#
# current_year = int(input())
# happy_year_gen = happy_year(current_year)
# print(next(happy_year_gen))

current_year = int(input())
while True:
    current_year += 1
    year_digits = ''
    for digit in str(current_year):
        if digit not in year_digits:
            year_digits += digit
        else:
            break
    else:
        happy_year = current_year
        break

print(happy_year)
