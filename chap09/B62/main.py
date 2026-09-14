# 再帰関数を使う問題はPyPyだとTLEになることがあるので注意！CPythonにしたほうがよい。
import sys

# 再帰呼び出しの深さの上限を深くする
sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self, i) -> None:
        self.i = i
        self.index = i + 1
        self.to_nodes: list[Node] = []
        self.visited = False


N, M = map(int, input().split())
nodes: list[Node] = [Node(i) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].to_nodes.append(nodes[b])
    nodes[b].to_nodes.append(nodes[a])


answer = []


def dfs(node: Node):
    if node.i == N - 1:
        answer.append(node.index)
        return True
    node.visited = True
    for to_node in node.to_nodes:
        if not to_node.visited:
            result = dfs(to_node)
            if result:
                answer.append(node.index)
                return True
    return False


dfs(nodes[0])
answer.reverse()
print(*answer)
