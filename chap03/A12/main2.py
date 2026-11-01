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


N, K = map(int, input().split())
A = list(map(int, input().split()))


def output_after_second(t: int):
    if t == 0:
        return 0
    output = 0
    for a in A:
        output += t // a
    return output


answer = most_left_ok(0, 10**9, lambda t: output_after_second(t) >= K)
if answer is None:
    raise
print(answer)
