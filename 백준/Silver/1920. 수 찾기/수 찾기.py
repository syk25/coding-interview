from sys import stdin

input = stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_set = set(n_list)


for number in m_list:
    if number in n_set:
        print(1)
    else:
        print(0)
