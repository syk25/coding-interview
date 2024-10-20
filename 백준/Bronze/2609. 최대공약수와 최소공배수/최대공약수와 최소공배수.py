def sol():
    a, b = map(int, input().split())

    if a < b:
        temp = a
        a = b
        b = temp

    a_divisors = find_divisors(a)
    b_divisors = find_divisors(b)

    my_gcd = 0
    for x in b_divisors:
        if a % x == 0:
            my_gcd = x

    my_lcm = (a // my_gcd) * (b // my_gcd) * my_gcd

    print(my_gcd)
    print(my_lcm)


def find_divisors(n):
    my_divisors = [x for x in range(1, n + 1) if n % x == 0]
    return my_divisors

sol()