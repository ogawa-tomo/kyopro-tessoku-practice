N = int(input())
# X = []
# Y = []
# 座標(x, y)にいくつの点があるか
max = 1501
numP = []
for _ in range(max):
    numP.append([0] * max)
# print(numP)
for _ in range(N):
    x, y = map(int, input().split())
    # print(x, y)
    numP[x][y] += 1
    # X.append(x)
    # Y.append(y)
# print(numP)

# 座標(0, 0)から(x, y)までで合計いくつの点があるか
sumP = []
for _ in range(max):
    sumP.append([0] * max)
# print(sumP)
# x方向に累積和をとる
for y in range(1, max):
    for x in range(1, max):
        sumP[x][y] = sumP[x - 1][y] + numP[x][y]
# print(sumP)
# y方向に累積和をとる
for x in range(1, max):
    for y in range(1, max):
        sumP[x][y] = sumP[x][y - 1] + sumP[x][y]
        # print(sumP[x][y])

# print(sumP)

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(sumP[c][d] - sumP[c][b - 1] - sumP[a - 1][d] + sumP[a - 1][b - 1])
