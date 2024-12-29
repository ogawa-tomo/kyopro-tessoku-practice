# これだと、通らない。main2.pyで通る。

import heapq
import sys

max_distance = sys.maxsize


class Node:
    def __init__(self) -> None:
        self.distance = max_distance
        self.links: list[Link] = []
        self.finalized = False

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return str(self.distance)


class Link:
    def __init__(self, distance: int, to_node: Node):
        self.distance = distance
        self.to_node = to_node


N, M = map(int, input().split())
nodes: list[Node] = [Node() for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    node1 = nodes[a - 1]
    node2 = nodes[b - 1]
    node1.links.append(Link(c, node2))
    node2.links.append(Link(c, node1))


q: list[Node] = []
nodes[0].distance = 0

heapq.heappush(q, nodes[0])
while q:
    print(q)
    node = heapq.heappop(q)
    print("pop", node)

    # ここをコメントアウトすると通る
    if node.finalized:
        continue
    node.finalized = True

    for link in node.links:
        distance = node.distance + link.distance
        if distance < link.to_node.distance:
            link.to_node.distance = distance
            # print("distance", distance)
            heapq.heappush(q, link.to_node)
            print("add", link.to_node)
            # if distance == 28:
            #     print("距離が28")
            #     print("このときのq", q)
            #     print("ここからpop", heapq.heappop(q))
        # ここで、距離28のNodeをpushしているが、次のループでpopされたのは30であり、heapqがバグっているように見える
        # [27, 32, 30, 40, 36, 37, 40, 42, 48, 37]
        # pop 27
        # add 28
        # add 31
        # [30, 32, 37, 40, 28, 37, 40, 42, 31, 28, 31]
        # pop 30
        # キュー内にすでに追加済みのNodeのdistanceも含めてイジってしまうからおかしなことになる

for node in nodes:
    if node.distance == max_distance:
        print(-1)
    else:
        print(node.distance)
