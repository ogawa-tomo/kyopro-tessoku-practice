N, K = map(int, input().split())
A = list(map(int, input().split()))


def output_after_second(t):
    if t == 0:
        return 0
    output = 0
    for a in A:
        output += t // a
    return output


def is_ok(t):
    return output_after_second(t) >= K


ng = -1
ok = 1000000000 + 1
while (ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
