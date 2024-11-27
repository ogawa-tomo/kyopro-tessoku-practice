N, K = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
S = []
for a in A:
    sum += a
    S.append(sum)
# print(S)


# A[left_index]からA[right_index]まで買い物をしたときの和
def sumA(left_index, right_index):
    if left_index == 0:
        return S[right_index]
    return S[right_index] - S[left_index - 1]


# R[i]: A[i]からA[R[i]]まで買い物をしたとき、K円を超えないような最大の数
R = [0] * N
for i in range(N):
    if i == 0:
        R[0] = 0
    else:
        R[i] = R[i - 1]

    while R[i] < N - 1 and sumA(i, R[i] + 1) <= K:
        R[i] += 1

answer = 0
for i in range(N):
    if R[i] == i and A[i] > K:
        continue
    answer += R[i] - i + 1

print(answer)
