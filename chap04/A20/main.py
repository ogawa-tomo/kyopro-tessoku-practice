S = list(input())
T = list(input())
# print(S)
S.insert(0, None)
T.insert(0, None)
# print(S)


# dp[i][j]: Sのi文字目、Tのj文字目までを使ったとき、最長の部分文字列
dp = []
for _ in range(len(S)):
    dp.append([0] * len(T))

for i in range(len(S)):
    for j in range(len(T)):
        if i == 0 or j == 0:
            dp[i][j] = 0
            continue
        if S[i] == T[j]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1], dp[i - 1][j])
            continue
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp[len(S) - 1][len(T) - 1])
