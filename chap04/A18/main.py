N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = []
for _ in range(N):
    dp.append([False] * (S + 1))
# print(dp)
if S == 0 or S == A[0]:
    print("Yes")
    exit()

dp[0][0] = True
if A[0] < S:
    dp[0][A[0]] = True

for i in range(1, N):
    for before_value in range(S):
        if dp[i - 1][before_value]:
            dp[i][before_value] = True
            if before_value + A[i] == S:
                print("Yes")
                exit()
            if before_value + A[i] > S:
                continue
            dp[i][before_value + A[i]] = True

print("No")
