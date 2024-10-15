from sys import stdin

input = stdin.readline

my_arr = [False] * 30

for i in range(28):
    idx = int(input()) - 1
    my_arr[idx] = True

answer = [0, 0]
j =0
for i in range(30):
    if my_arr[i] == False:
        answer[j] = i
        j += 1

for i in range(2):
    print(answer[i] + 1)