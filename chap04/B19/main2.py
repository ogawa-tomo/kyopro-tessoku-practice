import sys

N, W = map(int, input().split())


class Good:
    def __init__(self, weight: int, value: int):
        self.weight = weight
        self.value = value


goods: list[Good] = []
for _ in range(N):
    w, v = map(int, input().split())
    good = Good(w, v)
    goods.append(good)

# dp[n][v]: n個までの品物を選び、価値がvであるとき、重さの最小値
max_value = 1000 * N  # あり得る価値の最大値
dp: list[list[int]] = []
dp.append([sys.maxsize] * (max_value + 1))
dp[0][0] = 0
for n in range(1, N + 1):
    good = goods[n - 1]
    dp_n: list[int] = []
    for v in range(max_value + 1):
        if v - good.value >= 0:
            weight = min(dp[n - 1][v], dp[n - 1][v - good.value] + good.weight)
        else:
            weight = dp[n - 1][v]
        dp_n.append(weight)
    dp.append(dp_n)

# dp[N][v]をvの大きいほうから見ていき、最初に重さがW以下だったものが答え
# print(dp)
for v in range(max_value, -1, -1):
    if dp[N][v] <= W:
        print(v)
        exit()
