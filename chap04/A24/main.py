N = int(input())
A = list(map(int, input().split()))

answer = 0

# dp[i]: 最後の要素がAiである部分列のうち、最長のものの長さ
dp: list[int] = []

# L[x]: 長さxの部分列の最後の要素として考えられる値の最小値
L: list[int] = [0]

for a in A:
    length = len(L)

    # ok: 値がa未満であるLのインデックスの最大値
    ok = 0
    ng = length
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if L[mid] < a:
            ok = mid
        else:
            ng = mid

    # 最後の要素がaである部分列のうち、最長のものの長さ
    max_length = ok + 1
    dp.append(max_length)

    # Lを更新
    if length > max_length:
        L[max_length] = min(L[max_length], a)
    else:
        L.append(a)

print(max(dp))
