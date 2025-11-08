import sys

N, W = map(int, input().split())


class Good:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


goods: list[Good] = []
for _ in range(N):
    weight, value = map(int, input().split())
    good = Good(weight, value)
    goods.append(good)


# dp[i][j]: i番目までの品物を選び、重さの合計がjのとき、実現できる価値の最大値
dp: list[list[int]] = []
dp.append([-sys.maxsize] * (W + 1))
dp[0][0] = 0
# print(dp)
for i in range(1, N + 1):
    good = goods[i - 1]
    dp_row: list[int] = []
    for j in range(W + 1):
        if j - good.weight >= 0:
            value = max(dp[i - 1][j], dp[i - 1][j - good.weight] + good.value)
        else:
            value = dp[i - 1][j]
        dp_row.append(value)
    dp.append(dp_row)

print(max(dp[N]))
