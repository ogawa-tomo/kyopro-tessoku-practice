N = int(input())
h = list(map(int, input().split()))

#
# def cost(start, goal):

dp = [None] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))
# print(dp[N - 1])

answer = []
place = N - 1
while True:
    answer.append(place + 1)
    if place == 0:
        break
    if dp[place - 1] + abs(h[place] - h[place - 1]) == dp[place]:
        place -= 1
    else:
        place -= 2

answer.reverse()
print(len(answer))
print(" ".join(map(str, answer)))
