from sys import stdin

input = stdin.readline

def sol():
    l = int(input())
    string = input()
    M = 1234567891
    my_sum = 0
    for i in range(l):
        my_sum += hash_func(string[i], i)
    result = my_sum % M
    print(result)


def hash_func(c, i):
    n = ord(c) - ord("a") + 1
    r = 31
    return n * pow(r, i)


sol()
