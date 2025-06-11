def tribonacii(element: int):
    tribonacii_list = [1, 1, 2]
    if element > 3:
        for i in range(element-3):
            tribonacii_list.append(tribonacii_list[-1]+tribonacii_list[-2]+tribonacii_list[-3])

    return " ".join(map(str, tribonacii_list[:element]))


number_of_elements = int(input())
print(tribonacii(number_of_elements))
