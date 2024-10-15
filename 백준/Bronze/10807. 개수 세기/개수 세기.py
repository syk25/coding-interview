n = int(input())
my_arr = [x for x in map(int, input().split())]
v = int(input())

count = 0

for x in my_arr:
    if x == v:
        count += 1

print(count) 