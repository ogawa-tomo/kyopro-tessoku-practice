# AC
from collections import defaultdict, deque
import sys
import math


sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_nodes: list[Node] = []
        self.distance: int | None = None  # スタートからの距離
        self.visited = False
        self.color = 0

    def __repr__(self) -> str:
        return str(self.i + 1)


def bfs(start_node: Node):
    d: deque[Node] = deque()

    d.append(start_node)
    start_node.distance = 0
    while d:
        node = d.popleft()
        if node.distance is None:
            raise
        distance = node.distance
        for to_node in node.to_nodes:
            if to_node.distance is None:
                d.append(to_node)
                to_node.distance = distance + 1


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
    for node in nodes:
        node.visited = False
    gp = GetPath(nodes, start, goal)
    return gp.get_path()


# 木についての直径パスを求める
def get_diameter_path_for_tree(nodes: list[Node]):
    bfs(nodes[0])

    farthest_node = nodes[0]
    distance = 0
    for node in nodes:
        if node.distance is None:
            raise
        if node.distance > distance:
            farthest_node = node
            distance = node.distance

    for node in nodes:
        node.distance = None

    bfs(farthest_node)

    farthest_node2 = farthest_node
    distance = 0
    for node in nodes:
        if node.distance is None:
            raise
        if node.distance > distance:
            farthest_node2 = node
            distance = node.distance

    diameter_path = get_path(nodes, farthest_node, farthest_node2)
    return diameter_path


N = int(input())

nodes = [Node(i) for i in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.to_nodes.append(node_v)
    node_v.to_nodes.append(node_u)


C = list(map(int, input().split()))
for i in range(N):
    c = C[i]
    nodes[i].color = c

diameter_path = get_diameter_path_for_tree(nodes)
if diameter_path is None:
    raise
diameter = len(diameter_path) - 1

if diameter % 2 == 0:
    center = diameter_path[diameter // 2]

    target_distance = diameter // 2

    candidate_colors: set[int] = set()

    candidates: list[Node] = []
    for node in nodes:
        node.distance = None
    bfs(center)
    for node in nodes:
        if node.distance == target_distance:
            candidates.append(node)
            candidate_colors.add(node.color)

    num_candidates_by_color: defaultdict[int, int] = defaultdict(int)
    for node in candidates:
        num_candidates_by_color[node.color] += 1

    answer = 0
    for c in candidate_colors:
        answer += math.comb(num_candidates_by_color[c], 2)

    for node in nodes:
        node.visited = False
    for neighbor in center.to_nodes:
        candidates: list[Node] = []
        candidate_colors: set[int] = set()

        def dfs_without_center(node: Node):
            node.visited = True
            if node.distance == target_distance:
                candidates.append(node)
                candidate_colors.add(node.color)
            for to_node in node.to_nodes:
                if to_node == center:
                    continue
                if not to_node.visited:
                    dfs_without_center(to_node)

        dfs_without_center(neighbor)

        num_candidates_by_color = defaultdict(int)
        for node in candidates:
            num_candidates_by_color[node.color] += 1

        for c in candidate_colors:
            answer -= math.comb(num_candidates_by_color[c], 2)

else:
    center1 = diameter_path[diameter // 2]
    center2 = diameter_path[(diameter // 2) + 1]

    target_distance = (diameter - 1) // 2

    candidate_colors: set[int] = set()

    # 片方の中心からもう片方の中心を通らずtarget_distanceの距離にあるもの
    candidates_c1: list[Node] = []
    for node in nodes:
        node.distance = None
    d: deque[Node] = deque()
    d.append(center1)
    center1.distance = 0
    while d:
        node = d.popleft()
        if node.distance is None:
            raise
        distance = node.distance
        if distance == target_distance:
            candidates_c1.append(node)
            candidate_colors.add(node.color)
        for to_node in node.to_nodes:
            if to_node == center2:
                continue
            if to_node.distance is None:
                d.append(to_node)
                to_node.distance = distance + 1

    candidates_c2: list[Node] = []
    for node in nodes:
        node.distance = None
    d: deque[Node] = deque()
    d.append(center2)
    center2.distance = 0
    while d:
        node = d.popleft()
        if node.distance is None:
            raise
        distance = node.distance
        if distance == target_distance:
            candidates_c2.append(node)
            candidate_colors.add(node.color)
        for to_node in node.to_nodes:
            if to_node == center1:
                continue
            if to_node.distance is None:
                d.append(to_node)
                to_node.distance = distance + 1

    num_candidates_c1_by_color: defaultdict[int, int] = defaultdict(int)
    for node in candidates_c1:
        num_candidates_c1_by_color[node.color] += 1
    num_candidates_c2_by_color: defaultdict[int, int] = defaultdict(int)
    for node in candidates_c2:
        num_candidates_c2_by_color[node.color] += 1

    answer = 0
    for c in candidate_colors:
        answer += num_candidates_c1_by_color[c] * num_candidates_c2_by_color[c]

print(answer)
