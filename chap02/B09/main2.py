class Cover:
    def __init__(self, min_i: int, min_j: int, max_i: int, max_j: int):
        self.min_i = min_i
        self.min_j = min_j
        self.max_i = max_i
        self.max_j = max_j


class Covered2D:
    def __init__(self, covers: list[Cover], H: int, W: int):

        # (i, j)における差分
        x: list[list[int]] = []
        for _ in range(H + 1):
            x.append([0] * (W + 1))
        for cover in covers:
            x[cover.min_i][cover.min_j] += 1
            x[cover.min_i][cover.max_j + 1] -= 1
            x[cover.max_i + 1][cover.min_j] -= 1
            x[cover.max_i + 1][cover.max_j + 1] += 1

        # 累積和を求める
        self.grids: list[list[int]] = []
        for _ in range(H):
            self.grids.append([0] * W)
        for i in range(H):
            for j in range(W):
                if j == 0:
                    self.grids[i][j] = x[i][j]
                    continue
                self.grids[i][j] = self.grids[i][j - 1] + x[i][j]
        for j in range(W):
            for i in range(H):
                if i == 0:
                    continue
                self.grids[i][j] = self.grids[i - 1][j] + self.grids[i][j]


N = int(input())
grid_length = 1500


covers: list[Cover] = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    c -= 1
    d -= 1
    covers.append(Cover(a, b, c, d))

grids = Covered2D(covers, grid_length, grid_length).grids

answer = 0
for x in range(grid_length):
    for y in range(grid_length):
        if grids[x][y] >= 1:
            answer += 1
print(answer)
