from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

q: deque[int] = deque()
answer = 0
for a in A:
    q.append(a)
    diff = q[-1] - q[0]

    while diff > K:
        q.popleft()
        diff = q[-1] - q[0]

    answer += len(q) - 1

print(answer)
