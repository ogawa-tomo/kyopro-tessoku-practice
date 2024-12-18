N, M = map(int, input().split())

g: list[list[int]] = []
for _ in range(N):
    g.append([])

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

max_num = 0
answer = 0
for i, s in enumerate(g):
    num = len(g[i])
    if num > max_num:
        max_num = num
        answer = i + 1

print(answer)
