n = int(input())
answer = 0

for i in range(n):
    number_str = str(i)
    number = i
    for j in number_str:
        number += int(j)
    if number == n:
        answer = i
        break    

print(answer)