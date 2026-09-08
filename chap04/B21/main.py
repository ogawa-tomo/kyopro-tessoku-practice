N = int(input())
S = input()

# dp[l][r]: 文字列Sのl文字目からr文字目までの部分における最長回文の長さ
dp: list[list[int]] = []
for _ in range(N):
    dp.append([0] * N)

# print(dp)
for length in range(N):
    for left in range(N - length):
        right = left + length
        if left == right:
            dp[left][right] = 1
        elif left + 1 == right:
            dp[left][right] = 2 if S[left] == S[right] else 1
        else:
            if S[left] == S[right]:
                p1 = dp[left + 1][right - 1] + 2  # 中に両端足す
                p2 = dp[left][right - 1]  # 左側
                p3 = dp[left + 1][right]  # 右側
                dp[left][right] = max(p1, p2, p3)
            else:
                dp[left][right] = max(dp[left][right - 1], dp[left + 1][right])

# for row in dp:
#     print(row)
print(dp[0][N - 1])
