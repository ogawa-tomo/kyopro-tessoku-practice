N, K = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
right = 0
for left in range(N):
    while right < N - 1 and A[right + 1] - A[left] <= K:
        right += 1
    answer += right - left

print(answer)
