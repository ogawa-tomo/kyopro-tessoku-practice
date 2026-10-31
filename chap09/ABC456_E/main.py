import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_nodes: list[Node] = []
        self.visited = False
        self.finished = False
        self.is_holiday = False

    def __repr__(self) -> str:
        return str(self.i)


# サイクル検出
class CycleDetection:
    def __init__(self, nodes: list[Node]) -> None:
        self.nodes = nodes
        self.history: list[Node] = []

    def dfs(self, node: Node) -> Node | None:
        node.visited = True
        self.history.append(node)
        for to_node in node.to_nodes:
            if to_node.finished:
                continue
            if to_node.visited:
                # サイクル検出
                return to_node

            cycle_start_node = self.dfs(to_node)
            if cycle_start_node is not None:
                return cycle_start_node

        node.finished = True
        self.history.pop()

    def get_cycle(self, detection_start_node: Node):
        cycle_start_node = self.dfs(detection_start_node)
        if cycle_start_node is None:
            return None
        cycle: list[Node] = []
        while self.history:
            node = self.history.pop()
            cycle.append(node)
            if node == cycle_start_node:
                break
        cycle.reverse()
        return cycle


def get_cycle(nodes: list[Node], detection_start_node: Node):
    cd = CycleDetection(nodes)
    return cd.get_cycle(detection_start_node)


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    uv_list: list[tuple[int, int]] = []
    for _ in range(M):
        u, v = map(int, input().split())
        uv_list.append((u, v))
    W = int(input())
    S: list[str] = []
    for _ in range(N):
        s = input()
        S.append(s)

    all_cities = [Node(i) for i in range(N * W)]

    cities_by_num: defaultdict[int, list[Node]] = defaultdict(list)
    for i in range(N * W):
        city = all_cities[i]
        city_num = i // W
        cities_by_num[city_num].append(city)
        day = i % W
        if S[city_num][day] == "o":
            city.is_holiday = True

    # 今日と明日が休日ならパスがある
    for i in range(N):
        cities = cities_by_num[i]
        for day in range(W):
            city = cities[day]
            next_day_city = cities[(day + 1) % W]
            if city.is_holiday and next_day_city.is_holiday:
                city.to_nodes.append(next_day_city)

    # 今いる都市の今日と道の繋がった都市の明日が休日ならパスがある
    for u, v in uv_list:
        u -= 1
        v -= 1
        cities_u = cities_by_num[u]
        cities_v = cities_by_num[v]
        for today in range(W):
            tomorrow = (today + 1) % W
            city_u_today = cities_u[today]
            city_u_tomorrow = cities_u[tomorrow]
            city_v_today = cities_v[today]
            city_v_tomorrow = cities_v[tomorrow]

            if city_u_today.is_holiday and city_v_tomorrow.is_holiday:
                city_u_today.to_nodes.append(city_v_tomorrow)
            if city_v_today.is_holiday and city_u_tomorrow.is_holiday:
                city_v_today.to_nodes.append(city_u_tomorrow)

    ok = False
    for city_num in range(N):
        # 曜日1の都市を順に調べる
        city = cities_by_num[city_num][0]
        if not city.is_holiday:
            continue
        if city.visited:
            continue
        cycle = get_cycle(all_cities, city)
        if cycle is not None:
            ok = True
            break
    if ok:
        print("Yes")
    else:
        print("No")
