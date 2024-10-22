from sys import stdin

input = stdin.readline


n = int(input())
my_numbers = [int(input()) for _ in range(n)]
my_numbers.sort()
print(*my_numbers, sep="\n")
