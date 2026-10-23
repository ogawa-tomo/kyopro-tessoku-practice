# PyPyならACだがCPythonだとTLE
from collections import deque
import sys

# 再帰呼び出しの深さの上限を深くする
sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


# 強連結成分分解（Kosarajuのアルゴリズム）
class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_links: list[Link] = []
        self.from_links: list[Link] = []
        self.visited = False
        self.count = 0
        self.scc_id = 0
        self.scc_element: SCCElement = SCCElement()

    def __repr__(self) -> str:
        return str(self.i)


# Linkを介してるのはこの問題の事情でリンクの性質を持ちたいからであって、一般に強連結成分分解をしたいだけならLinkは必要ない
class Link:
    def __init__(self, from_node: Node, to_node: Node, equal: bool) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.equal = equal


class SCCElement:
    def __init__(self) -> None:
        self.nodes: set[Node] = set()
        self.to_elements: set[SCCElement] = set()
        self.from_elements: set[SCCElement] = set()
        self.num = 0

    def __repr__(self) -> str:
        return str(self.nodes)


class SCCKosaraju:
    def __init__(self, nodes: list[Node]) -> None:
        self.nodes = nodes
        self.count = 1
        for node in self.nodes:
            if not node.visited:
                self.outbound_dfs(node)

        for node in self.nodes:
            node.visited = False

        sorted_nodes = sorted(self.nodes, key=lambda n: n.count, reverse=True)
        self.scc_elements: list[SCCElement] = []
        for node in sorted_nodes:
            if not node.visited:
                scc_element = SCCElement()
                self.inbound_dfs(node, scc_element)
                self.scc_elements.append(scc_element)

        for node in nodes:
            scc_element = node.scc_element
            for to_link in node.to_links:
                to_element = to_link.to_node.scc_element
                if to_element != scc_element:
                    scc_element.to_elements.add(to_element)
                    to_element.from_elements.add(scc_element)

    def outbound_dfs(self, node: Node):
        node.visited = True
        for to_link in node.to_links:
            to_node = to_link.to_node
            if not to_node.visited:
                self.outbound_dfs(to_node)
        node.count = self.count
        self.count += 1

    def inbound_dfs(self, node: Node, scc_element: SCCElement):
        node.visited = True
        scc_element.nodes.add(node)
        node.scc_element = scc_element
        for from_link in node.from_links:
            from_node = from_link.from_node
            if not from_node.visited:
                self.inbound_dfs(from_node, scc_element)


def get_scc_elements(nodes: list[Node]):
    scc_kosaraju = SCCKosaraju(nodes)
    return scc_kosaraju.scc_elements


N, Q = map(int, input().split())

nodes = [Node(i + 1) for i in range(N)]
for _ in range(Q):
    t, u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    link = Link(node_u, node_v, t == 0)
    node_u.to_links.append(link)
    node_v.from_links.append(link)


scc_elements = get_scc_elements(nodes)

# 強連結成分内に不等号があればNG
for element in scc_elements:
    for node in element.nodes:
        for to_link in node.to_links:
            if to_link.to_node in element.nodes and not to_link.equal:
                print("No")
                exit()

root_elements: list[SCCElement] = []
for element in scc_elements:
    if not element.from_elements:
        root_elements.append(element)

# DAGのトポロジカルソート
sorted_elements: list[SCCElement] = []
d: deque[SCCElement] = deque()
for element in root_elements:
    d.append(element)
while d:
    element = d.popleft()
    sorted_elements.append(element)
    for to_element in element.to_elements:
        to_element.from_elements.remove(element)
        if not to_element.from_elements:
            d.append(to_element)

# トポロジカルソートの結果で番号をつける
for i in range(len(sorted_elements)):
    element = sorted_elements[i]
    element.num = i + 1

print("Yes")
print(*[node.scc_element.num for node in nodes])
