from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n, x = map(int, input().split())

my_arr = [i for i in map(int, input().split())]

for e in my_arr:
    if e < x:
        print("%d " % e)
