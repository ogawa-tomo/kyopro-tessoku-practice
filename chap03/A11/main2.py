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


# 二分探索
def most_left_ok(min_i: int, max_i: int, ok_func: Callable[[int], bool]):
    ok = max_i + 1
    ng = min_i - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if ok_func(mid):
            ok = mid
        else:
            ng = mid
    if ok > max_i:
        return None
    return ok


N, X = map(int, input().split())
A = list(map(int, input().split()))
i = most_right_ok(0, N - 1, lambda i: A[i] <= X)
# i = most_left_ok(0, N - 1, lambda i: A[i] >= X)  # こっちでもOK
if i is None:
    raise
print(i + 1)
