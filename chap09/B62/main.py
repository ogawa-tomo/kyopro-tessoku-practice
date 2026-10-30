# 再帰関数を使う問題はPyPyだとTLEになることがあるので注意！CPythonにしたほうがよい。
import sys

# 再帰呼び出しの深さの上限を深くする
sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self, i) -> None:
        self.i = i
        self.to_nodes: list[Node] = []
        self.visited = False

    def __repr__(self) -> str:
        return str(self.i + 1)


class GetPath:
    def __init__(self, nodes: list[Node], start: Node, goal: Node) -> None:
        self.nodes = nodes
        self.start = start
        self.goal = goal
        self.path: list[Node] = []

    def dfs(self, node: Node):
        node.visited = True
        if node == self.goal:
            self.path.append(node)
            return True
        for to_node in node.to_nodes:
            if not to_node.visited and self.dfs(to_node):
                self.path.append(node)
                return True
        return False

    def get_path(self):
        if self.dfs(self.start):
            self.path.reverse()
            return self.path


def get_path(nodes: list[Node], start: Node, goal: Node):
    gp = GetPath(nodes, start, goal)
    return gp.get_path()


N, M = map(int, input().split())
nodes: list[Node] = [Node(i) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].to_nodes.append(nodes[b])
    nodes[b].to_nodes.append(nodes[a])

path = get_path(nodes, nodes[0], nodes[N - 1])
if path is not None:
    print(*path)
# この問題ではpathは必ず存在する前提
