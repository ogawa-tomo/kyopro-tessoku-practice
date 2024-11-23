N, Q = map(int, input().split())
A = list(map(int, input().split()))
LR = []
for _ in range(Q):
    L, R = map(int, input().split())
    LR.append([L, R])

accumulate_A = []
total = 0
for a in A:
    total += a
    accumulate_A.append(total)

for lr in LR:
    l = lr[0] - 1
    r = lr[1] - 1
    if l != 0:
        print(accumulate_A[r] - accumulate_A[l - 1])
    else:
        print(accumulate_A[r])
