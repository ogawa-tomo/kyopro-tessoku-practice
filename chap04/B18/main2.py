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

if not dp[N][S]:
    print(-1)
    exit()

cards: list[int] = []
s = S
# n枚目のカードを選ぶべきかを判定する
for n in range(N, 0, -1):
    a = A[n - 1]
    if dp[n - 1][s]:
        # n-1枚目まででsが実現できていれば、n枚目を選ぶ必要はない
        pass
    elif dp[n - 1][s - a]:
        # n-1枚目まででs-aが実現できていれば、n枚目を選ぶ
        cards.append(n)
        s -= a
    else:
        # これはありえない
        raise

cards.reverse()
print(len(cards))
print(*cards)
