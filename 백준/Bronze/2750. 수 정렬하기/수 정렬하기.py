from sys import stdin

input = stdin.readline


def selection_sort(my_list):
    
    my_size = len(my_list)
    for i in range(my_size - 1):
        min_idx = i
        for j in range(i + 1, my_size):
            if my_list[min_idx] >= my_list[j]:
                min_idx = j
        my_list[min_idx], my_list[i] = my_list[i], my_list[min_idx]
    return


n = int(input())
my_numbers = [int(input()) for _ in range(n)]
selection_sort(my_numbers)
print(*my_numbers, sep="\n")
