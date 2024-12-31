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


N, Q = map(int, input().split())

nodes = [Node() for _ in range(N)]
for _ in range(Q):
    t, u, v = map(int, input().split())
    u -= 1
    v -= 1
    root_u = nodes[u].root()
    root_v = nodes[v].root()
    if t == 1:
        if root_u == root_v:
            continue
        if root_u.size < root_v.size:
            root_u.parent = root_v
            root_v.size += root_u.size
        else:
            root_v.parent = root_u
            root_u.size += root_v.size

    elif t == 2:
        if root_u == root_v:
            print("Yes")
        else:
            print("No")
