N = int(input())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# row[i]: i行目はもともとの何行目か
row = list(range(N))
Q = int(input())
for _ in range(Q):
    q, x, y = map(int, input().split())
    x -= 1
    y -= 1

    if q == 1:
        temp_row_x = row[x]
        row[x] = row[y]
        row[y] = temp_row_x
    if q == 2:
        print(grid[row[x]][y])
