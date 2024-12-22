from collections import deque


class Node:
    def __init__(self, row, column, is_node) -> None:
        self.row = row
        self.column = column
        self.is_node = is_node
        self.neighbors: list[Node] = []
        self.distance = 0
        self.finalized = False

    def set_distance(self, distance):
        self.finalized = True
        self.distance = distance

    def __repr__(self):
        if self.is_node:
            return "."
        else:
            return "#"


R, C = map(int, input().split())

sy, sx = map(int, input().split())
sy -= 1
sx -= 1

gy, gx = map(int, input().split())
gy -= 1
gx -= 1

nodes: list[list[Node]] = []
for r in range(R):
    row_data = list(input())
    row: list[Node] = []
    for c in range(C):
        grid = row_data[c]
        if grid == "#":
            node = Node(r, c, False)
        elif grid == ".":
            node = Node(r, c, True)
        row.append(node)
    nodes.append(row)

# print(nodes)


for r in range(1, R - 1):
    for c in range(1, C - 1):
        node = nodes[r][c]
        if not node.is_node:
            continue
        # 上
        upper_node = nodes[r - 1][c]
        if upper_node.is_node:
            node.neighbors.append(upper_node)
        # 左
        left_node = nodes[r][c - 1]
        if left_node.is_node:
            node.neighbors.append(left_node)
        # 右
        right_node = nodes[r][c + 1]
        if right_node.is_node:
            node.neighbors.append(right_node)
        # 下
        bottom_node = nodes[r + 1][c]
        if bottom_node.is_node:
            node.neighbors.append(bottom_node)

d: deque[Node] = deque()
start_node = nodes[sy][sx]
start_node.set_distance(0)
d.append(start_node)
while len(d) > 0:
    node = d.popleft()
    for neighbor in node.neighbors:
        if not neighbor.finalized:
            neighbor.set_distance(node.distance + 1)
            d.append(neighbor)
            if neighbor.row == gy and neighbor.column == gx:
                print(neighbor.distance)
                exit()
