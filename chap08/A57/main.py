N, Q = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] -= 1

max_digit = 30

# dp[i][j]: 穴jにいた2**i日後の場所
dp: list[list[int]] = []
for _ in range(max_digit):
    dp.append([0] * N)

dp[0] = A
for i in range(1, max_digit):
    for j in range(N):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]
# print(dp)


for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    current = x
    for k in range(max_digit, -1, -1):
        if y & (1 << k):
            current = dp[k][current]
    print(current + 1)
