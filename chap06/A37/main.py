N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

print(sum(A) * M + sum(C) * N + M * N * B)
