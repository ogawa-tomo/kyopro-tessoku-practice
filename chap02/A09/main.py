H, W, N = map(int, input().split())

# 点(x, y)における差分
X = []
for _ in range(H + 1):
    X.append([0] * (W + 1))
for _ in range(N):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    X[a][b] += 1
    X[a][d + 1] -= 1
    X[c + 1][b] -= 1
    X[c + 1][d + 1] += 1

# 点(x, y)における累積和
Z = []
for _ in range(H):
    Z.append([0] * W)
for i in range(H):
    for j in range(W):
        if j == 0:
            Z[i][0] = X[i][0]
            continue
        Z[i][j] = Z[i][j - 1] + X[i][j]
for j in range(W):
    for i in range(H):
        if i == 0:
            continue
        Z[i][j] = Z[i - 1][j] + Z[i][j]

for i in range(H):
    for j in range(W):
        if j >= 1:
            print(" ", end="")
        print(Z[i][j], end="")
    print("")
