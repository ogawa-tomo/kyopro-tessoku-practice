# WA
from collections import deque


class Grid:
    def __init__(self, i: int, j: int, is_white: bool):
        self.i = i
        self.j = j
        self.is_white = is_white
        self.to_grids: list[Grid] = []
        self.patterns = 0
        self.added_count = 0

    def __repr__(self):
        return str(self.patterns)
        # if self.is_white:
        #     return "."
        # else:
        #     return "#"


H, W = map(int, input().split())

grids: list[list[Grid]] = []
for i in range(H):
    data = list(input())
    row: list[Grid] = []
    for j, da in enumerate(data):
        grid = Grid(i, j, da == ".")
        row.append(grid)
    grids.append(row)

# print(grids)
for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if not grid.is_white:
            continue
        # 下
        if i < H - 1:
            below = grids[i + 1][j]
            if below.is_white:
                grid.to_grids.append(below)
        # 右
        if j < W - 1:
            right = grids[i][j + 1]
            if right.is_white:
                grid.to_grids.append(right)


d: deque[Grid] = deque()

start = grids[0][0]
d.append(start)
start.patterns = 1
while d:
    grid = d.popleft()
    patterns = grid.patterns
    for to_grid in grid.to_grids:
        if to_grid.added_count < 2:
            to_grid.patterns += patterns
            to_grid.added_count += 1
            d.append(to_grid)

print(grids)
print(grids[H - 1][W - 1].patterns)
