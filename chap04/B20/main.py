S = input()
T = input()

dp: list[list[int]] = []
for i in range(len(S) + 1):
    dp.append([0] * (len(T) + 1))

# print(dp)
for i in range(len(S) + 1):
    for j in range(len(T) + 1):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + 1
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + 1
        else:
            c = 0 if S[i - 1] == T[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + c)

print(dp[len(S)][len(T)])
