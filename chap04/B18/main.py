N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = []
for _ in range(N):
    dp.append([False] * (S + 1))


dp[0][0] = True
if A[0] == S:
    print(1)
    print(1)
    exit()
elif A[0] < S:
    dp[0][A[0]] = True

for i in range(1, N):
    for j in range(S + 1):
        if not (dp[i - 1][j]):
            continue
        dp[i][j] = True
        if j + A[i] <= S:
            dp[i][j + A[i]] = True

if not (dp[N - 1][S]):
    print(-1)
    exit()

card_number = N - 1
number = S
answer = []
while True:
    if card_number == 0:
        if number > 0:
            answer.append(0)
        break
    if number - A[card_number] >= 0 and dp[card_number - 1][number - A[card_number]]:
        answer.append(card_number)
        number -= A[card_number]
    card_number -= 1

# print(dp)
answer.reverse()
print(len(answer))
print(" ".join(map(str, [a + 1 for a in answer])))
