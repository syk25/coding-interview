def find_max_sum(cards, n, m):
    max_sum = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                current_sum = cards[i] + cards[j] + cards[k]
                if current_sum <= m:
                    if max_sum < current_sum:
                        max_sum = current_sum

    return max_sum


from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
cards = [x for x in map(int, input().split())]

print(find_max_sum(cards, n, m))
