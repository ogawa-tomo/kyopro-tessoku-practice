from collections import defaultdict, deque


H, W, K = map(int, input().split())


class Node:
    def __init__(self, empty: bool) -> None:
        self.is_empty = empty
        self.to_nodes: list[Node] = []
        self.distance: int | None = None  # スタートからの距離


# 多始点BFS
def bfs(start_nodes: list[Node]):
    answer = 0
    d: deque[Node] = deque()

    for node in start_nodes:
        d.append(node)
        node.distance = 0
        answer += 1
    while d:
        node = d.popleft()
        if node.distance is None:
            raise
        distance = node.distance
        for to_node in node.to_nodes:
            if to_node.distance is None:
                d.append(to_node)
                to_node.distance = distance + 1
                if to_node.distance <= K:
                    answer += 1
    return answer


nodes: list[list[Node]] = []
for i in range(H):
    S = input()
    row: list[Node] = []
    for s in S:
        node = Node(s == ".")
        row.append(node)
    nodes.append(row)

for i in range(H):
    for j in range(W):
        node = nodes[i][j]

        di_list = [1, 0, -1, 0]
        dj_list = [0, 1, 0, -1]
        for d in range(4):
            ii = i + di_list[d]
            jj = j + dj_list[d]
            if 0 <= ii and ii < H and 0 <= jj and jj < W:
                to_node = nodes[ii][jj]
                if to_node.is_empty:
                    node.to_nodes.append(to_node)

is_safety_by_i: defaultdict[int, bool] = defaultdict(bool)
for i in range(H):
    is_safety = True
    for j in range(W):
        node = nodes[i][j]
        if not node.is_empty:
            is_safety = False
            break
    is_safety_by_i[i] = is_safety

is_safety_by_j: defaultdict[int, bool] = defaultdict(bool)
for j in range(W):
    is_safety = True
    for i in range(H):
        node = nodes[i][j]
        if not node.is_empty:
            is_safety = False
            break
    is_safety_by_j[j] = is_safety

safety_nodes: list[Node] = []
for i in range(H):
    for j in range(W):
        node = nodes[i][j]
        if is_safety_by_i[i] and is_safety_by_j[j]:
            safety_nodes.append(node)

answer = bfs(safety_nodes)
print(answer)
