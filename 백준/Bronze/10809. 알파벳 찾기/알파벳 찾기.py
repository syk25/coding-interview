word = input()

my_chars = [-1 for _ in range(26)]

for i in range(len(word)):
    idx = len(word) - 1 - i
    loc = ord(word[idx]) - ord("a")
    my_chars[loc] = idx

print(*my_chars)
