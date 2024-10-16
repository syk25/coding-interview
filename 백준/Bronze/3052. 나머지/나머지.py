left_overs = set()

for _ in range(10):
    left_overs.add(int(input()) % 42)

print(len(left_overs))
