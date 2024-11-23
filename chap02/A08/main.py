H, W = map(int, input().split())
X = []
for _ in range(H):
    x = list(map(int, input().split()))
    X.append(x)
# print(X)
Q = int(input())

# Zの初期化
Z = []
for _ in range(H):
    z = [0] * W
    Z.append(z)

# 横方向の累積和
for i in range(H):
    for j in range(W):
        if j == 0:
            Z[i][j] = X[i][0]
        else:
            Z[i][j] = Z[i][j - 1] + X[i][j]
# 縦方向に累積和をとる
for j in range(W):
    for i in range(H):
        if i == 0:
            continue
        Z[i][j] = Z[i - 1][j] + Z[i][j]

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if a == 0 and b == 0:
        print(Z[c][d])
    elif a == 0 and b > 0:
        print(Z[c][d] - Z[c][b - 1])
    elif a > 0 and b == 0:
        print(Z[c][d] - Z[a - 1][d])
    else:
        print(Z[c][d] - Z[c][b - 1] - Z[a - 1][d] + Z[a - 1][b - 1])
