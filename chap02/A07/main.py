D = int(input())
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    L.append(l)
    R.append(r)

# 出席者数の前日比
B = [0] * (D + 1)
for i in range(N):
    B[L[i]] += 1
    B[R[i] + 1] -= 1

# 累積和
s = 0
for d in range(D):
    s += B[d]
    print(s)
