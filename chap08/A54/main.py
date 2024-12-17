Q = int(input())

d = {}
for _ in range(Q):
    q = list(input().split())
    if q[0] == "1":
        name = q[1]
        point = int(q[2])
        d[name] = point
    if q[0] == "2":
        name = q[1]
        print(d[name])
