list_words = input().split()
palindrome = input()
palindrome_list = [word for word in list_words if word[::-1] == word]
count_of_palindrome = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {count_of_palindrome} times")