N, W = map(int, input().split())
V = 1000 * N


class Good:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


goods = []
for _ in range(N):
    weight, value = map(int, input().split())
    good = Good(weight, value)
    goods.append(good)


# dp[i][j]: i番目までの品物を選び、価値の合計がjのとき、実現できる重さの最小値
dp = []
for _ in range(N):
    dp.append([None] * (V + 1))

dp[0][0] = 0
good = goods[0]
dp[0][good.value] = good.weight

for i in range(1, N):
    good = goods[i]
    for j in range(V + 1):
        candidates = []
        if dp[i - 1][j] is not None:
            candidates.append(dp[i - 1][j])
        if j - good.value >= 0 and dp[i - 1][j - good.value] is not None:
            candidates.append(dp[i - 1][j - good.value] + good.weight)
        if len(candidates) == 0:
            continue
        dp[i][j] = min(candidates)

# print(dp)

answer = 0
for value, weight in enumerate(dp[N - 1]):
    if weight is None:
        continue
    if weight > W:
        continue
    answer = value
print(answer)
