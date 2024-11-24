N = int(input())
max = 1500

# 座標(x, y)にある紙の差分
X = []
for _ in range(max + 1):
    X.append([0] * (max + 1))
for _ in range(N):
    a, b, c, d = map(int, input().split())
    X[a][b] += 1
    X[a][d] -= 1
    X[c][b] -= 1
    X[c][d] += 1

# 座標(x, y)にある紙の累積和
# Z = []
# for _ in range(max + 1):
#     Z.append([0] * (max + 1))
# 横方向に累積和をとる
for y in range(0, max + 1):
    for x in range(1, max + 1):
        X[x][y] = X[x - 1][y] + X[x][y]
# 縦方向に累積和をとる
for x in range(0, max + 1):
    for y in range(1, max + 1):
        X[x][y] = X[x][y - 1] + X[x][y]

answer = 0
for x in range(max + 1):
    for y in range(max + 1):
        if X[x][y] >= 1:
            answer += 1
print(answer)
