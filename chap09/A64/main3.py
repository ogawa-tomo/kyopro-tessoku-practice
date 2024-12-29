import heapq


q: list[int] = [3, 2, 2, 4, 1]
heapq.heapify(q)
while q:
    print(heapq.heappop(q))


class Node:
    def __init__(self, distance: int) -> None:
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return str(self.distance)


print()
q2: list[Node] = [Node(3), Node(2), Node(2), Node(4), Node(1)]
heapq.heapify(q2)
while q2:
    print(heapq.heappop(q2))

print()
node2 = Node(2)
q3: list[Node] = [Node(3), node2, Node(4), Node(1)]
heapq.heapify(q3)
heapq.heappush(q3, node2)
node2.distance = 10  # queueに追加済みのオブジェクトの属性をイジるとバグる！
while q3:
    print(heapq.heappop(q3))
