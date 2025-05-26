number_of_lines = int(input())
balanced = True
text = ""

for i in range(number_of_lines):
    string = input()
    if string == "(":
        if text == "":
            text += string
        else:
            balanced = False
    if string == ")":
        if text == "(":
            text = ""
        else:
            balanced = False
if text != "":
    balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")