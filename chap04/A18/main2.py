N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[n][s]: n枚目までのカードを選んで、値をsにすることができるか
dp: list[list[bool]] = []
dp.append([False] * (S + 1))
dp[0][0] = True
for n in range(1, N + 1):
    a = A[n - 1]
    dp_n: list[bool] = []
    for s in range(S + 1):
        if dp[n - 1][s]:
            dp_n.append(True)
            continue
        if s - a >= 0 and dp[n - 1][s - a]:
            dp_n.append(True)
            continue
        dp_n.append(False)
    dp.append(dp_n)

if dp[N][S]:
    print("Yes")
else:
    print("No")
