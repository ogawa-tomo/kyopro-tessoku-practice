from collections import deque

Q = int(input())
stack: deque[str] = deque()

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        stack.append(query[1])
    if query[0] == "2":
        print(stack[-1])
    if query[0] == "3":
        stack.pop()
