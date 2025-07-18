char_1 = ord(input())
char_2 = ord(input())
string = [x for x in input()]
ascii_sum = sum(map(lambda x: ord(x), list(filter(lambda x: ord(x) in range(min(char_1, char_2)+1, max(char_1, char_2)), string))))
print(ascii_sum)