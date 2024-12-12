N = int(input())


class Point:
    def __init__(self, block_idx, point):
        self.block_idx = block_idx
        self.point = point


points = []
for _ in range(N):
    block_idx, point = map(int, input().split())
    block_idx -= 1
    points.append(Point(block_idx, point))

# dp[l][r]: l番目からr番目までのブロックが残っているとき、最大の点数
dp = []
for _ in range(N):
    dp.append([None] * N)

dp[0][N - 1] = 0

for length in range(N - 1, 0, -1):
    # print(length)
    for left in range(N - length + 1):
        right = left + length - 1
        # dp[left][right]を求めたい。
        candidates = [0]

        # dp[left][right + 1]から右側を取り除く場合
        if right < N - 1:
            p = points[right + 1]
            current_point = dp[left][right + 1]
            if left <= p.block_idx and p.block_idx <= right:
                candidates.append(current_point + p.point)
            else:
                candidates.append(current_point)

        # dp[left - 1][right]から左側を取り除く場合
        if left > 0:
            p = points[left - 1]
            current_point = dp[left - 1][right]

            if left <= p.block_idx and p.block_idx <= right:
                candidates.append(current_point + p.point)
            else:
                candidates.append(current_point)

        # print(left, right)
        dp[left][right] = max(candidates)

answer = 0
for i in range(N):
    answer = max(answer, dp[i][i])
print(answer)
