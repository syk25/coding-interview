for _ in range(int(input())):
    k = int(input())
    n = int(input())
    my_list = [x for x in range(n + 1)]
    for _ in range(k):
        for i in range(n):
            my_list[i + 1] = my_list[i + 1] + my_list[i]
    print(my_list[-1])
