n = int(input())

for line in range(n):
    for space in range(1, n - line):
        print(" ", end="")
    for star in range(line + 1):
        print("*", end="")
    print()
