N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(A)
# A = [0, 0].extend(A)
A = [0, 0] + A
B = [0, 0, 0] + B
# print(A)
# print(B)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    if i == 1:
        dp[1] = 0
        continue
    if i == 2:
        dp[2] = A[2]
        continue
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

print(dp[N])
