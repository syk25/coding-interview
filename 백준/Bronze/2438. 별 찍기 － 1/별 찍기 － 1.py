n = int(input())

for line in range(1, n + 1):
    for star in range(0, line):
        print("*", end="")
    print()
