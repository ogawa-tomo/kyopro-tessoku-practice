from typing import Callable


# 二分探索
def most_right_ok(min_i: int, max_i: int, ok_func: Callable[[int], bool]):
    ok = min_i - 1
    ng = max_i + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if ok_func(mid):
            ok = mid
        else:
            ng = mid
    if ok < min_i:
        return None
    return ok


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()
for _ in range(Q):
    x = int(input())
    i = most_right_ok(0, N - 1, lambda i: A[i] < x)
    if i is None:
        print(0)
    else:
        print(i + 1)
