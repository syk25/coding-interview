from sys import stdin

input = stdin.readline

n = int(input())
my_list = [int(input()) for _ in range(n)]

my_list.sort()

print(*my_list, sep="\n")
