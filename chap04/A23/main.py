import sys

N, M = map(int, input().split())


# dp[i][j]: i枚目のクーポンまでで、jが示す品物のセットを買うのに必要なクーポンの最小枚数
dp: list[list[int]] = []
for _ in range(M + 1):
    dp.append([sys.maxsize] * (1 << N))

dp[0][0] = 0


for i in range(1, M + 1):
    A = list(map(int, input().split()))

    # クーポンで買える品物のセット
    goods = 0
    for k, a in enumerate(A):
        if a:
            # k番目の品物が買える
            goods |= 1 << k

    for j in range(1 << N):
        # クーポンを使わないケース
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        # クーポンを使うケース
        dp[i][j | goods] = min(dp[i][j | goods], dp[i - 1][j] + 1)

answer = dp[M][(1 << N) - 1]
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
