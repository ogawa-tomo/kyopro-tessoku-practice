N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [0, 0] + A
B = [0, 0, 0] + B

dp = [0] * (N + 1)
dp[1] = 0
dp[2] = A[2]
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

place = N
answer = []
while True:
    answer.append(place)
    if place == 1:
        break
    if dp[place - 1] + A[place] == dp[place]:
        place -= 1
    else:
        place -= 2

answer.reverse()
print(len(answer))
print(" ".join(map(str, answer)))
