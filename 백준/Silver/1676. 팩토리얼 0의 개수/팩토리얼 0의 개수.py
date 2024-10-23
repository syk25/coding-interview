n = int(input())

two_count = 0
five_count = 0

for number in range(1, n + 1):

    while number % 2 == 0:
        two_count += 1
        number //= 2

    while number % 5 == 0:
        five_count += 1
        number //= 5

print(min(two_count, five_count))
