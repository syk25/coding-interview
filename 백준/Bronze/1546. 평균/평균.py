n = int(input())
scores = list(map(int, input().split()))
scores.sort()

M = scores[-1]

for i in range(n):
    scores[i] = scores[i] / M * 100

print(sum(scores) / n)
