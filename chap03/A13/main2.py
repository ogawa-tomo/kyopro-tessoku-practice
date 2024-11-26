N, K = map(int, input().split())
A = list(map(int, input().split()))

# A.sort()

answer = 0
for i in range(1, N):
    a = A[i - 1]
    arr = A[i:]
    # print(a)
    # print(arr)
    n = len(arr)

    def is_ok(index):
        if index < 0:
            return True
        if index >= n:
            return False
        return arr[index] - a <= K

    ok = -1
    ng = n
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    # print(ok + 1)
    # print()
    answer += ok + 1

print(answer)
