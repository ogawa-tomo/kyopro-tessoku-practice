from collections import deque


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        self.distance: int | None = None  # 頂点0からの距離


N, M = map(int, input().split())

nodes = [Node() for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].neighbors.append(nodes[b])
    nodes[b].neighbors.append(nodes[a])

d: deque[Node] = deque()

d.append(nodes[0])
nodes[0].distance = 0
while d:
    node = d.popleft()
    if node.distance is None:
        raise
    distance = node.distance
    for neighbor in node.neighbors:
        if neighbor.distance is None:
            d.append(neighbor)
            neighbor.distance = distance + 1

for node in nodes:
    if node.distance is None:
        print(-1)
    else:
        print(node.distance)
