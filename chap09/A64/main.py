import heapq
import sys

max_distance = sys.maxsize


class Node:
    def __init__(self) -> None:
        self.distance = max_distance
        self.links: list[Link] = []
        self.finalized = False

    def __repr__(self):
        return str(self.distance)


class Link:
    def __init__(self, distance: int, to_node: Node):
        self.distance = distance
        self.to_node = to_node


# キューには同じノードが追加されることがある。
# キューに追加済みのノードに対してdistanceを操作すると、キューが正常に動作しない。
# したがって、キューに追加するための専用のクラスを用意する。
class QueueObject:
    def __init__(self, node: Node):
        self.node = node
        self.distance = node.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return str(self.distance)


def dijkstra(start_node: Node):
    q: list[QueueObject] = []
    start_node.distance = 0

    heapq.heappush(q, QueueObject(start_node))
    while q:
        queue_object = heapq.heappop(q)
        node = queue_object.node

        if node.finalized:
            continue
        node.finalized = True

        for link in node.links:
            distance = node.distance + link.distance
            if distance < link.to_node.distance:
                link.to_node.distance = distance
                heapq.heappush(q, QueueObject(link.to_node))


N, M = map(int, input().split())
nodes: list[Node] = [Node() for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    node1 = nodes[a - 1]
    node2 = nodes[b - 1]
    node1.links.append(Link(c, node2))
    node2.links.append(Link(c, node1))

dijkstra(nodes[0])

for node in nodes:
    if node.distance == max_distance:
        print(-1)
    else:
        print(node.distance)
