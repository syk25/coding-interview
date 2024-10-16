my_numbers = [x for x in map(int, input().split())]

d1 = 0
for i in range(len(my_numbers) - 2):
    d1 = my_numbers[i + 1] - my_numbers[i]
    d2 = my_numbers[i + 2] - my_numbers[i + 1]
    if d1 != d2:
        d1 = 2
        break


if d1 == 1:
    print("ascending")
elif d1 == -1:
    print("descending")
else:
    print("mixed")
