from sys import stdin

input = stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    print(a + b)


