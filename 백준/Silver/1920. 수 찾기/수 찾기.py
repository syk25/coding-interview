from sys import stdin

input = stdin.readline


def sol():
    n = int(input())
    n_list = list(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))

    # n_list를 정렬
    n_list.sort()
    # m_list의 각 수별로 이진탐색 후 있으면 1 반환 없으면 0 반환
    for number in m_list:
        print(binary_search(n_list, number))


def binary_search(my_list, number):

    l = 0
    r = len(my_list) - 1

    while l <= r:
        mid = (l + r) // 2
        if number < my_list[mid]:
            r = mid - 1
        elif number > my_list[mid]:
            l = mid + 1
        else:
            return 1
    return 0

sol()