keys = input().split(", ")
words = input().split(", ")
keys_in_words = [key for key in keys if any(key in word for word in words)]

print(keys_in_words)