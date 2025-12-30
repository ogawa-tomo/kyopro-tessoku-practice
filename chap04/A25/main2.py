class Grid:
    def __init__(self, i: int, j: int, is_white: bool):
        self.i = i
        self.j = j
        self.is_white = is_white
        self.patterns = 0

    def __repr__(self):
        return str(self.patterns)


H, W = map(int, input().split())

grids: list[list[Grid]] = []
for i in range(H):
    data = list(input())
    row: list[Grid] = []
    for j, da in enumerate(data):
        grid = Grid(i, j, da == ".")
        row.append(grid)
    grids.append(row)

grids[0][0].patterns = 1
for i in range(H):
    for j in range(W):
        grid = grids[i][j]

        if not grid.is_white:
            continue

        if i > 0:
            above = grids[i - 1][j]
            grid.patterns += above.patterns
        if j > 0:
            left = grids[i][j - 1]
            grid.patterns += left.patterns

# print(grids)
print(grids[H - 1][W - 1].patterns)
