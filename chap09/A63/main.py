from collections import deque
from typing import Union


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        self.distance = -1  # 頂点0からの距離


N, M = map(int, input().split())
nodes: list[Node] = []
for _ in range(N):
    nodes.append(Node())

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].neighbors.append(nodes[b])
    nodes[b].neighbors.append(nodes[a])

d: deque[Node] = deque()

d.append(nodes[0])
nodes[0].distance = 0
while len(d) > 0:
    node = d.popleft()
    distance = node.distance
    for neighbor in node.neighbors:
        if neighbor.distance == -1:
            d.append(neighbor)
            neighbor.distance = distance + 1

for node in nodes:
    print(node.distance)
