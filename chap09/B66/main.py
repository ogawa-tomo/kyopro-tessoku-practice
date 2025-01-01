from typing import Union

import sys

sys.setrecursionlimit(1000000)


class Station:
    def __init__(self) -> None:
        # self.neighbors: list[Station] = []
        self.parent: Union[None, Station] = None
        self.size = 1

    def root(self):
        if self.parent is None:
            return self
        return self.parent.root()


class Line:
    def __init__(self, station_1: Station, station_2: Station):
        self.station_1 = station_1
        self.station_2 = station_2
        self.cancelled = False


def unite(line: Line):
    root_1 = line.station_1.root()
    root_2 = line.station_2.root()
    if root_1 == root_2:
        return
    if root_1.size < root_2.size:
        root_1.parent = root_2
        root_2.size += root_1.size
    else:
        root_2.parent = root_1
        root_1.size += root_2.size


def is_connected(station_1: Station, station_2: Station):
    return station_1.root() == station_2.root()


N, M = map(int, input().split())
stations = [Station() for _ in range(N)]

lines: list[Line] = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    station_1 = stations[a]
    station_2 = stations[b]
    lines.append(Line(station_1, station_2))


answers = []


class Query1:
    def __init__(self, x: int):
        self.x = x

    def execute(self):
        unite(lines[self.x])


class Query2:
    def __init__(self, u: int, v: int):
        self.u = u
        self.v = v

    def execute(self):
        if is_connected(stations[self.u], stations[self.v]):
            answers.append("Yes")
        else:
            answers.append("No")


queries: list[Union[Query1, Query2]] = []
Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    # print(q)
    if q[0] == 1:
        x = q[1] - 1
        lines[x].cancelled = True
        queries.append(Query1(x))

    else:
        u = q[1] - 1
        v = q[2] - 1
        queries.append(Query2(u, v))

# その日の最後の状態を再現するために、
# キャンセルされていない路線をつなげる
for line in lines:
    if not line.cancelled:
        unite(line)

# 後ろからクエリを処理する
for query in reversed(queries):
    query.execute()

for answer in reversed(answers):
    print(answer)
