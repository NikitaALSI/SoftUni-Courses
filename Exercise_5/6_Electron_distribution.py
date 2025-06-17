def get_shell_distribution(electrons: int):
    electron_distribution = []
    shell = 0
    while electrons > 0:
        shell += 1
        if 2 * shell**2 <= electrons:
            electron_distribution.append(2 * shell**2)
        else:
            electron_distribution.append(electrons)
        electrons -= 2 * shell**2
    return electron_distribution


number_of_electrons = int(input())
print(get_shell_distribution(number_of_electrons))