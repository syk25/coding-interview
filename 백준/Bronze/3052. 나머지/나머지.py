my_numbers = [int(input()) for _ in range(10)]

left_overs = set()

for number in my_numbers:
    left_overs.add(number % 42)

print(len(left_overs))
