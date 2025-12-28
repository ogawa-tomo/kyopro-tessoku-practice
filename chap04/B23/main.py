import math
import sys

N = int(input())


class City:
    def __init__(self, i: int, x: int, y: int):
        self.i = i
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.i, self.x, self.y))


def travel_time(c1: City, c2: City):
    return math.sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)


cities: list[City] = []
for i in range(N):
    x, y = map(int, input().split())
    city = City(i, x, y)
    cities.append(city)

# print(cities)

# dp[i][j]: iの示す都市を通っていて、いま都市jにいるときの距離
dp: list[list[int]] = []
for _ in range(1 << N):
    dp.append([sys.maxsize] * N)

# 都市N-1から出発したという扱いで、都市0..N-1に最初にいくときの距離を入力する
for i in range(N - 1):
    dp[1 << i][i] = travel_time(cities[i], cities[N - 1])
    # print(dp[1 << i][i])
# print(dp)

for i in range(1, 1 << N):
    # いま、iの表す都市を通った
    for j in range(N):
        # いま、都市jにいる
        for k in range(N):
            # これから都市kにいく
            if i & (1 << k):
                # 既に都市kを通っていれば無視
                continue
            to = i | (1 << k)
            dp[to][k] = min(dp[to][k], dp[i][j] + travel_time(cities[j], cities[k]))
            # print(to, k, dp[to][k])

# 最後にいる都市はN-1である必要がある（1周して戻ってくるから）
print(dp[(1 << N) - 1][N - 1])
