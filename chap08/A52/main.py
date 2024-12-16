from collections import deque

d: deque[str] = deque()

Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        d.append(q[1])
    if q[0] == "2":
        print(d[0])
    if q[0] == "3":
        d.popleft()
