N, K = map(int, input().split())
A = list(map(int, input().split()))

# R[i]: A[R[i]] - A[i] <= Kであるような最大の値
R = [0] * N
for i in range(N):
    if i == 0:
        R[0] = 0
    else:
        R[i] = R[i - 1]

    while R[i] < N - 1 and A[R[i] + 1] - A[i] <= K:
        R[i] += 1

answer = 0
for i in range(N):
    answer += R[i] - i

print(answer)
