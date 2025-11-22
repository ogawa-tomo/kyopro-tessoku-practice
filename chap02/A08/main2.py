class CumulativeSum2D:
    def __init__(self, grids: list[list[int]]):
        self.grids = grids
        self.cum_sum_grids: list[list[int]] = []
        for i in range(len(grids)):
            row_cum_sum: list[int] = []
            total = 0
            for j in range(len(grids[i])):
                total += grids[i][j]
                row_cum_sum.append(total)
            self.cum_sum_grids.append(row_cum_sum)
        for i in range(len(grids)):
            if i == 0:
                continue
            for j in range(len(grids[i])):
                self.cum_sum_grids[i][j] += self.cum_sum_grids[i - 1][j]

    def range_sum(self, min_i, min_j, max_i, max_j):
        if min_i == 0 and min_j == 0:
            return self.cum_sum_grids[max_i][max_j]
        elif min_i == 0 and min_j > 0:
            return (
                self.cum_sum_grids[max_i][max_j] - self.cum_sum_grids[max_i][min_j - 1]
            )
        elif min_i > 0 and min_j == 0:
            return (
                self.cum_sum_grids[max_i][max_j] - self.cum_sum_grids[min_i - 1][max_j]
            )
        else:
            return (
                self.cum_sum_grids[max_i][max_j]
                - self.cum_sum_grids[max_i][min_j - 1]
                - self.cum_sum_grids[min_i - 1][max_j]
                + self.cum_sum_grids[min_i - 1][min_j - 1]
            )


H, W = map(int, input().split())
grids: list[list[int]] = []

for _ in range(H):
    row = list(map(int, input().split()))
    grids.append(row)

cum_sum_2d = CumulativeSum2D(grids)

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    print(cum_sum_2d.range_sum(a, b, c, d))
