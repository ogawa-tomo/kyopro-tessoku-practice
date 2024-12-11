N, W = map(int, input().split())


class Good:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


goods = []
for _ in range(N):
    weight, value = map(int, input().split())
    good = Good(weight, value)
    goods.append(good)


# dp[i][j]: i番目までの品物を選び、重さの合計がjのとき、実現できる価値の最大値
dp = []
for _ in range(N):
    dp.append([None] * (W + 1))

dp[0][0] = 0
good = goods[0]
if good.weight <= W:
    dp[0][good.weight] = good.value

for i in range(1, N):
    good = goods[i]
    for j in range(W + 1):
        candidates = []
        if dp[i - 1][j] is not None:
            candidates.append(dp[i - 1][j])
        if j - good.weight >= 0 and dp[i - 1][j - good.weight] is not None:
            candidates.append(dp[i - 1][j - good.weight] + good.value)
        if len(candidates) == 0:
            continue
        dp[i][j] = max(candidates)

# print(dp[N - 1])
values = []
for v in dp[N - 1]:
    if v is not None:
        values.append(v)

# print(values)
print(max(values))
