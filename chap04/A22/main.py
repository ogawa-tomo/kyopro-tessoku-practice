N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [-(10**9)] * N
dp[0] = 0
for i in range(N - 1):
    a = A[i] - 1
    b = B[i] - 1
    dp[a] = max(dp[i] + 100, dp[a])
    dp[b] = max(dp[i] + 150, dp[b])
# print(dp)
# print(max(dp))
print(dp[N - 1])
