from sys import stdin, stdout

input = stdin.readline

t = int(input())


def sol():
    h, w, n = map(int, input().split())

    y = n % h
    x = n // h + 1

    if y == 0:
        y = h
        x = n // h

    y = str(y)

    if x < 10:
        x = "0" + str(x)

    x = str(x)
    print(int(y + x))


for _ in range(t):
    sol()
