from sys import stdin

input = stdin.readline

a = int(input())
b = int(input())
c = int(input())

number_str = str(a * b * c)

my_numbers = [0 for x in range(10)]

for c in number_str:
    my_numbers[int(c)] += 1

print(*my_numbers, sep="\n")
