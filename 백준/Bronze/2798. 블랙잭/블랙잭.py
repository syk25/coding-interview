from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

cards = [x for x in map(int, input().split())]
cards.sort()

deck_bag = set()

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            temp = cards[i] + cards[j] + cards[k]
            deck_bag.add(temp)

deck_bag = list(deck_bag)
deck_bag.sort()

my_max = deck_bag[0]

for number in deck_bag:
    if number > m:
        break
    if my_max < number:
        my_max = number

print(my_max)
