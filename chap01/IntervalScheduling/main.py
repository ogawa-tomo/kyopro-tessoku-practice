# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_b


class Interval:
    def __init__(self, left: int, right: int) -> None:
        self.left = left
        self.right = right


N = int(input())

intervals: list[Interval] = []
for _ in range(N):
    a, b = map(int, input().split())
    interval = Interval(a, b)
    intervals.append(interval)

intervals.sort(key=lambda i: i.right)

answer = 0
prev: Interval | None = None
for interval in intervals:
    if prev is None or prev.right < interval.left:
        prev = interval
        answer += 1

print(answer)
