t = int(input())

for _ in range(t):
    n, word = input().split()
    n = int(n)

    result = ""
    for c in word:
        result += c * n
    print(result)
