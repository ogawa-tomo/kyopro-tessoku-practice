from collections import deque


class Node:
    def __init__(self) -> None:
        self.to_nodes: list[Node] = []
        self.distance: int | None = None  # スタートからの距離


def bfs(start_node: Node):
    d: deque[Node] = deque()

    d.append(start_node)
    start_node.distance = 0
    while d:
        node = d.popleft()
        if node.distance is None:
            raise
        distance = node.distance
        for to_node in node.to_nodes:
            if to_node.distance is None:
                d.append(to_node)
                to_node.distance = distance + 1


N, M = map(int, input().split())
A = list(map(int, input().split()))
nodes = [Node() for _ in range(2**N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    z -= 1
    for s in range(1 << N):
        from_node = nodes[s]
        trans = (1 << x) + (1 << y) + (1 << z)
        to_node = nodes[s ^ trans]
        from_node.to_nodes.append(to_node)

start = 0
for i, a in enumerate(A):
    start += a * (1 << i)
start_node = nodes[start]
goal_node = nodes[(1 << N) - 1]

bfs(start_node)

if goal_node.distance is None:
    print(-1)
else:
    print(goal_node.distance)
