n = int(input())

my_list = [x for x in map(int, input().split())]

my_min = my_list[0]
my_max = my_list[0]

for number in my_list:
    if my_min > number:
        my_min = number

for number in my_list:
    if my_max < number:
        my_max = number


print(my_min, my_max)
