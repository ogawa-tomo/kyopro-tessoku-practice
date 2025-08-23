from typing import Union
import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self) -> None:
        self.parent: Union[None, Node] = None
        self.size = 1

    def root(self):
        if self.parent is None:
            return self
        return self.parent.root()


def is_same(node1: Node, node2: Node):
    return node1.root() == node2.root()


def unite(node1: Node, node2: Node):
    root1 = node1.root()
    root2 = node2.root()
    if root1.size < root2.size:
        root1.parent = root2
        root2.size += root1.size
    else:
        root2.parent = root1
        root1.size += root2.size


N, Q = map(int, input().split())

nodes = [Node() for _ in range(N)]

for _ in range(Q):
    t, u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    if t == 1:
        if is_same(node_u, node_v):
            continue
        unite(node_u, node_v)
    elif t == 2:
        if is_same(node_u, node_v):
            print("Yes")
        else:
            print("No")
