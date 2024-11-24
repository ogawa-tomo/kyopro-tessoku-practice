import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()
# print(A)

# print(bisect.bisect_left(A, 17))

Q = int(input())
for _ in range(Q):
    x = int(input())
    print(bisect.bisect_left(A, x))
