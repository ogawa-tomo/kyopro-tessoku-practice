from typing import Callable


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


N, K = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
for left in range(N - 1):
    a = A[left]
    right = most_right_ok(left + 1, N - 1, lambda r: A[r] - a <= K)
    if right is None:
        continue
    answer += right - left

print(answer)
