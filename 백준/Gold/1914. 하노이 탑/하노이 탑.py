def hanoi_count(n: int):
    if n == 1:
        return 1
    return 2 * hanoi_count(n - 1) + 1


def hanoi_movement(n, src, dest, temp):
    if n == 1:
        print(src, dest)
        return
    elif n == 2:
        print(src, temp)
        print(src, dest)
        print(temp, dest)
        return
    else:
        hanoi_movement(n - 1, src, temp, dest)
        hanoi_movement(1, src, dest, temp)
        hanoi_movement(n - 1, temp, dest, src)


n = int(input())
print(hanoi_count(n))
if n <= 20:
    hanoi_movement(n, 1, 3, 2)
