n = int(input())

my_list = [x for x in map(int, input().split())]

my_list.sort()

print(my_list[0], my_list[-1])
