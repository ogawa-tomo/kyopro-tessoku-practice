from typing import Union
import sys

sys.setrecursionlimit(10**9)


class Node:
    def __init__(self) -> None:
        self.parent: Union[None, Node] = None
        self.size = 1

    @property
    def root(self):
        if self.parent is None:
            return self
        return self.parent.root


def is_same(node1: Node, node2: Node):
    return node1.root == node2.root


def unite(node1: Node, node2: Node):
    root1 = node1.root
    root2 = node2.root
    if root1 == root2:
        raise
    if root1.size < root2.size:
        root1.parent = root2
        root2.size += root1.size
    else:
        root2.parent = root1
        root1.size += root2.size


class Link:
    def __init__(self, node_a: Node, node_b: Node, c: int) -> None:
        self.node_a = node_a
        self.node_b = node_b
        self.c = c


N, M = map(int, input().split())

nodes = [Node() for _ in range(N)]
links: list[Link] = []
for _ in range(M):
    a, b, c = map(int, input().split())
    node_a = nodes[a - 1]
    node_b = nodes[b - 1]
    link = Link(node_a, node_b, c)
    links.append(link)

answer = 0
links.sort(key=lambda l: l.c, reverse=True)
for link in links:
    if not is_same(link.node_a, link.node_b):
        answer += link.c
        unite(link.node_a, link.node_b)
print(answer)
