from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    print("%d\n" % (a+b))


