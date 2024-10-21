n = int(input())
my_list = list(set([input() for _ in range(n)]))

my_list.sort()
my_list = sorted(my_list, key=lambda x: len(x))
print(*my_list, sep="\n")
