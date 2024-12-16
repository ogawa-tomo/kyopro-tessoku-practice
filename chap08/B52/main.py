from collections import deque

N, X = map(int, input().split())
A = list(input())

q: deque[int] = deque()

X -= 1
A[X] = "@"
q.append(X)
while len(q) > 0:
    index = q.popleft()
    if index - 1 >= 0 and A[index - 1] == ".":
        A[index - 1] = "@"
        q.append(index - 1)
    if index + 1 < N and A[index + 1] == ".":
        A[index + 1] = "@"
        q.append(index + 1)
print("".join(A))
