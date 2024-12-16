from collections import deque

d: deque[int] = deque()
S = list(input())
# print(S)

for i, s in enumerate(S):
    if s == "(":
        d.append(i)
    if s == ")":
        end = i
        start = d.pop()
        print(start + 1, end + 1)
