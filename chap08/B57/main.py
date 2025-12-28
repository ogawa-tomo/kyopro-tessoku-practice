N, K = map(int, input().split())

max_digit = 40

# dp[i][j]: jを2**i回操作した結果
dp: list[list[int]] = []
for _ in range(max_digit):
    dp.append([0] * (N + 1))

for j in range(N + 1):
    dp[0][j] = j - sum(list(map(int, list(str(j)))))
for i in range(1, max_digit):
    for j in range(N + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

# print(dp)

for j in range(1, N + 1):
    current = j
    for k in range(max_digit, -1, -1):
        if K & (1 << k):
            current = dp[k][current]
    print(current)
