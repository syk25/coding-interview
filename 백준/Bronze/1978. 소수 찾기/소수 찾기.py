def sol():

    n = int(input())
    numbers = [x for x in map(int, input().split())]
    count = 0
    for number in numbers:
        if check_prime(number):
            count += 1
    print(count)


def check_prime(number: int) -> bool:
    divisors = [x for x in range(1, number + 1) if number % x == 0]

    if len(divisors) == 2:
        return True
    else:
        return False


sol()
