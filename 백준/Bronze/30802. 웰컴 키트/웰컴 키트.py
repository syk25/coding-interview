from sys import stdin

input = stdin.readline

n = int(input())
applicants = [x for x in map(int, input().split())]
t, p = map(int, input().split())


t_count = 0

for s in applicants:
    if s % t == 0:
        t_count += s // t
    else:
        t_count += s // t + 1

p_count = n // p
p_left = n % p

print(t_count)
print(p_count, p_left)
