for _ in range(int(input())):
    total_points = 0
    count = 0

    for g in input():
        if g == "O":
            count += 1
            total_points += count
        else:
            count = 0

    print(total_points)
