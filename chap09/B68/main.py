# 再帰関数を使う問題はPyPyだとTLEになることがあるので注意！CPythonにしたほうがよい。
import sys

# 再帰呼び出しの深さの上限を深くする
sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self) -> None:
        self.to_links: list[Link] = []
        self.from_links: list[Link] = []
        self.used = False


class Link:
    def __init__(self, from_node: Node, to_node: Node, capacity: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.capacity = capacity
        self.flow = 0  # 順方向に流れている量

    # 順方向に流せる余地
    @property
    def forward_remaining(self):
        return self.capacity - self.flow

    # 逆方向に流せる余地
    @property
    def reverse_remaining(self):
        return self.flow


N, M = map(int, input().split())
P = list(map(int, input().split()))


nodes = [Node() for _ in range(N + 2)]
start = nodes[N]
goal = nodes[N + 1]
default = 0
for i, p in enumerate(P):
    node = nodes[i]
    if p > 0:
        from_start_link = Link(start, node, p)
        to_goal_link = Link(node, goal, 0)
        default += p
    else:
        from_start_link = Link(start, node, 0)
        to_goal_link = Link(node, goal, -p)
    start.to_links.append(from_start_link)
    node.from_links.append(from_start_link)
    node.to_links.append(to_goal_link)
    goal.from_links.append(to_goal_link)


for _ in range(M):
    a, b = map(int, input().split())
    node_a = nodes[a - 1]
    node_b = nodes[b - 1]
    link = Link(node_a, node_b, sys.maxsize)
    node_a.to_links.append(link)
    node_b.from_links.append(link)


def dfs(start: Node, goal: Node, flow: int):
    if start == goal:
        return flow
    start.used = True

    # 順方向を検討
    for to_link in start.to_links:
        if to_link.to_node.used:
            continue
        if to_link.forward_remaining == 0:
            continue

        f = dfs(to_link.to_node, goal, min(flow, to_link.forward_remaining))
        if f >= 1:
            to_link.flow += f
            return f

    # 逆方向を検討
    for from_link in start.from_links:
        if from_link.from_node.used:
            continue
        if from_link.reverse_remaining == 0:
            continue

        f = dfs(from_link.from_node, goal, min(flow, from_link.reverse_remaining))
        if f >= 1:
            from_link.flow -= f
            return f

    return 0


total_loss = 0
while True:
    for node in nodes:
        node.used = False
    loss = dfs(start, goal, sys.maxsize)
    if loss == 0:
        break
    total_loss += loss

print(default - total_loss)
