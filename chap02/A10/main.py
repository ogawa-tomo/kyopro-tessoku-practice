N = int(input())
A = list(map(int, input().split()))
D = int(input())
L = []
R = []

# 前からi番目の部屋までで最も大きい部屋
from_front_max = [0] * N
for i in range(N):
    if i == 0:
        from_front_max[0] = A[0]
        continue
    from_front_max[i] = max(from_front_max[i - 1], A[i])
# print(from_front_max)
from_back_max = [0] * N
for i in range(N):
    if i == 0:
        from_back_max[N - 1] = A[N - 1]
        continue
    from_back_max[N - 1 - i] = max(from_back_max[N - i], A[N - i - 1])
# print(from_back_max)

for _ in range(D):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(max(from_front_max[l - 1], from_back_max[r + 1]))
