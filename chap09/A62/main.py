# 再帰関数を使う問題はPyPyだとTLEになることがあるので注意！CPythonにしたほうがよい。
import sys

# 再帰呼び出しの深さの上限を深くする
sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった

N, M = map(int, input().split())


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        self.visited = False


nodes: list[Node] = []
for _ in range(N):
    nodes.append(Node())

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].neighbors.append(nodes[b])
    nodes[b].neighbors.append(nodes[a])
# print(nodes)


def dfs(node: Node):
    node.visited = True
    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor)


dfs(nodes[0])
for node in nodes:
    if not node.visited:
        print("The graph is not connected.")
        exit()
print("The graph is connected.")
