import sys

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self) -> None:
        self.to_nodes: list[Node] = []
        self.parent: Node | None = None
        self.subtree_size = 1
        self.x = 0


class Link:
    def __init__(self, i: int, left: Node, right: Node) -> None:
        self.i = i
        self.left = left
        self.right = right


# 部分木のサイズを調べる
# parentとsubtree_sizeの調査
def dfs(node: Node):
    subtree_size = 1
    for to_node in node.to_nodes:
        if to_node != node.parent:
            to_node.parent = node
            subtree_size += dfs(to_node)
    node.subtree_size = subtree_size
    return subtree_size


# xの計算（子孫に伝播させる）
def dfs2(node: Node):
    for to_node in node.to_nodes:
        if to_node != node.parent:
            to_node.x += node.x
            dfs2(to_node)


N = int(input())

nodes = [Node() for _ in range(N)]
links: list[Link] = []
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node_a = nodes[a]
    node_b = nodes[b]
    node_a.to_nodes.append(node_b)
    node_b.to_nodes.append(node_a)
    link = Link(i + 1, node_a, node_b)
    links.append(link)

dfs(nodes[0])

# リンクごとに、部分木の頂点に足すべきxを求める（子孫への伝播はあとで）
for link in links:
    if link.left.parent == link.right:
        parent = link.right
        child = link.left
    else:
        parent = link.left
        child = link.right

    child_subtree_size = child.subtree_size
    parent_subtree_size = N - child.subtree_size

    # 子が大きければ子に足し、親が大きければ根に足して子に引くことで親側だけに足す操作を実現
    if child_subtree_size > parent_subtree_size:
        child.x += link.i
    else:
        nodes[0].x += link.i
        child.x -= link.i

dfs2(nodes[0])

print(*[node.x for node in nodes])
