from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

q: deque[int] = deque()
total = 0
answer = 0
for a in A:
    q.append(a)
    total += a

    while total > K:
        drop = q.popleft()
        total -= drop

    answer += len(q)

print(answer)
