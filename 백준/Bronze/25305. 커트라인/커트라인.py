from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
my_numbers = list(map(int, input().split()))


def insertion_sort(my_list: list):

    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i
        for j in range(i, -1, -1):
            if my_list[j - 1] > key:
                my_list[j] = my_list[j - 1]
            else:
                break
        my_list[j] = key

    return my_list


print(insertion_sort(my_numbers)[-k])
