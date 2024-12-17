import heapq

Q = int(input())

a: list[int] = []
for _ in range(Q):
    q = list(input().split())
    if q[0] == "1":
        x = int(q[1])
        heapq.heappush(a, x)
    if q[0] == "2":
        print(a[0])
    if q[0] == "3":
        heapq.heappop(a)
