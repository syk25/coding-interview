a, b = map(int, input().split())

carry = 0

if b < 45:
    a -= 1
    b = b - 45 + 60
    if a < 0:
        a = 23
    print(a, b)
else:
    print(a, b - 45)
