class Scaffold:
    def __init__(self, height: int):
        self.height = height
        self.links: list[Link] = []
        self.cost = 0

    def calc_cost(self):
        self.cost = min([link.from_scaffold.cost + link.cost for link in self.links])


class Link:
    def __init__(self, cost: int, from_scaffold: Scaffold):
        self.cost = cost
        self.from_scaffold = from_scaffold


N = int(input())
H = list(map(int, input().split()))

scaffolds: list[Scaffold] = []
for i in range(N):
    h = H[i]
    scaffolds.append(Scaffold(h))
    if i >= 1:
        from_scaffold = scaffolds[i - 1]
        to_scaffold = scaffolds[i]
        cost = abs(from_scaffold.height - to_scaffold.height)
        link = Link(cost, from_scaffold)
        to_scaffold.links.append(link)
    if i >= 2:
        from_scaffold = scaffolds[i - 2]
        to_scaffold = scaffolds[i]
        cost = abs(from_scaffold.height - to_scaffold.height)
        link = Link(cost, from_scaffold)
        to_scaffold.links.append(link)

for i in range(1, N):
    scaffolds[i].calc_cost()

print(scaffolds[N - 1].cost)
