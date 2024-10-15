my_list = [int(input()) for _ in range(9)]

my_max = my_list[0]
idx = 0

for number in range(9):

    if my_max < my_list[number]:
        my_max = my_list[number]
        idx = number

print(my_max, idx + 1, sep="\n")
