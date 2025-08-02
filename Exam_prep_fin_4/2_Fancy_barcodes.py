import re


barcode_pat = r"(@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,})"
group_pat = r"\d"

number_of_barcodes = int(input())
for _ in range(number_of_barcodes):
    barcode = input()
    valid = re.match(barcode_pat, barcode)
    if valid:
        digits = re.findall(group_pat, valid.group(2))
        if digits:
            group = "".join(digits)
        else:
            group = "00"
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")
