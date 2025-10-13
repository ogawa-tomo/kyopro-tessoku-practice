# グラフを用いた方法
class Room:
    def __init__(self) -> None:
        self.time = 0
        self.routes: list[Route] = []

    def calc_time(self):
        self.time = min([route.from_room.time + route.time for route in self.routes])


class Route:
    def __init__(self, time: int, from_room: Room):
        self.time = time
        self.from_room = from_room


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rooms = [Room() for _ in range(N)]

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
print(rooms[N - 1].time)
