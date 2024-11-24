N, X = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = N - 1
while True:
    M = int((L + R) / 2)
    if X < A[M]:
        R = M - 1
    elif X == A[M]:
        print(M + 1)
        exit()
    else:
        L = M + 1
