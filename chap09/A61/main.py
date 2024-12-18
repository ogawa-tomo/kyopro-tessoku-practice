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

for i, n in enumerate(g):
    print(f"{i + 1}: {{{', '.join([str(j + 1) for j in g[i]])}}}")
