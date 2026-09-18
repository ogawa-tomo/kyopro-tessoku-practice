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

nodes = [Node() for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].to_nodes.append(nodes[b])
    nodes[b].to_nodes.append(nodes[a])

bfs(nodes[0])

for node in nodes:
    if node.distance is None:
        print(-1)
    else:
        print(node.distance)
