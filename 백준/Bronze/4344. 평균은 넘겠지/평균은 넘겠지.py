c = int(input())

for _ in range(c):
    case = list(map(int, input().split()))
    my_avg = sum(case[1:]) / case[0]
    sorted_case = sorted(case[1:])

    count = 0
    for grade in sorted_case:
        if grade > my_avg:
            count += 1
    ratio = 100 * count / case[0]
    print(ratio, "%")
