my_arr = [x for x in map(int, input().split(" "))]


my_sum = 0

for n in my_arr:
    my_sum += n**2

result = my_sum % 10
print(result)