import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

answer = 0
for i in range(1, N):
    a = A[i - 1]
    arr = A[i:]
    # print(a)
    # print(arr)
    min = 0
    max = len(arr) - 1
    while min < max:
        mid = math.ceil((min + max) / 2)
        if arr[mid] - a > K:
            max = mid - 1
        else:
            min = mid
    if min == 0 and arr[0] - a > K:
        continue
    answer += max + 1
    # print(max + 1)

print(answer)
