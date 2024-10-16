while True:
    my_numbers = [x for x in map(int, input().split())]

    if my_numbers[0] == 0:
        break

    my_numbers.sort()

    if my_numbers[0] ** 2 + my_numbers[1] ** 2 == my_numbers[2] ** 2:
        print("right")
    else:
        print("wrong")
