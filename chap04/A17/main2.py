# グラフを用いた方法
import sys


class Room:
    def __init__(self, i: int) -> None:
        self.i = i
        self.time = 0
        self.routes: list[Route] = []
        self.best_from_room: Room | None = None

    def calc_time(self):
        time = sys.maxsize
        for route in self.routes:
            route_time = route.from_room.time + route.time
            if route_time < time:
                time = route_time
                room = route.from_room
        self.time = time
        self.best_from_room = room


class Route:
    def __init__(self, time: int, from_room: Room):
        self.time = time
        self.from_room = from_room


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rooms = [Room(i) for i in range(N)]

for i in range(N - 1):
    a = A[i]
    from_room = rooms[i]
    to_room = rooms[i + 1]
    route = Route(a, from_room)
    to_room.routes.append(route)

for i in range(N - 2):
    b = B[i]
    from_room = rooms[i]
    to_room = rooms[i + 2]
    route = Route(b, from_room)
    to_room.routes.append(route)

for i in range(1, N):
    rooms[i].calc_time()

best_route: list[Room] = []
current_room: Room | None = rooms[N - 1]
while current_room:
    best_route.append(current_room)
    current_room = current_room.best_from_room

best_route.reverse()
# print(rooms[N - 1].time)
print(len(best_route))
print(" ".join([str(room.i + 1) for room in best_route]))
