class Node:
    def __init__(self) -> None:
        self.to_nodes: list[Node] = []
        self.visited = False


# スタックによる実装
def dfs(first_node: Node):
    stack: list[Node] = []
    first_node.visited = True
    stack.append(first_node)

    while stack:
        node = stack.pop()
        for to_node in node.to_nodes:
            if not to_node.visited:
                to_node.visited = True
                stack.append(to_node)


N, M = map(int, input().split())

nodes: list[Node] = []
for _ in range(N):
    nodes.append(Node())

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].to_nodes.append(nodes[b])
    nodes[b].to_nodes.append(nodes[a])

dfs(nodes[0])

for node in nodes:
    if not node.visited:
        print("The graph is not connected.")
        exit()
print("The graph is connected.")
