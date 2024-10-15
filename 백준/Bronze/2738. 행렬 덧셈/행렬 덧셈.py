n, m = map(int, input().split())

matrix1 = [[y for y in map(int, input().split())] for x in range(n)]
matrix2 = [[y for y in map(int, input().split())] for x in range(n)]

for x in range(n):
    for y in range(m):
        print(matrix1[x][y] + matrix2[x][y], end=" ")
    print()
