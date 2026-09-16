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


N = int(input())
students = [Node() for _ in range(N)]
seats = [Node() for _ in range(N)]
start = Node()
goal = Node()
for student in students:
    link = Link(start, student, 1)
    start.to_links.append(link)
    student.from_links.append(link)
for seat in seats:
    link = Link(seat, goal, 1)
    seat.to_links.append(link)
    goal.from_links.append(link)
for i in range(N):
    C = list(input())
    student = students[i]
    for j, c in enumerate(C):
        if c == ".":
            continue
        seat = seats[j]
        link = Link(student, seat, 1)
        student.to_links.append(link)
        seat.from_links.append(link)

answer = 0
while True:
    for student in students:
        student.used = False
    for seat in seats:
        seat.used = False
    start.used = False
    goal.used = False
    flow = dfs(start, goal, sys.maxsize)
    if flow == 0:
        break
    answer += flow

print(answer)
