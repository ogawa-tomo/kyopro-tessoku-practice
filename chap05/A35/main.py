N = int(input())
A = list(map(int, input().split()))

dp: list[list[int]] = []
for _ in range(N - 1):
    dp.append([0] * N)

dp.append(A)
# print(dp)
for i in range(N - 2, -1, -1):
    for j in range(i + 1):
        if i % 2 == 0:
            # 最大化
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])
        else:
            # 最小化
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1])

print(dp[0][0])
