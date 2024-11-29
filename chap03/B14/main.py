N, K = map(int, input().split())
A = list(map(int, input().split()))

half = N // 2
first_half_A = A[:half]
second_half_A = A[half:]
# print(first_half_A)
# print(second_half_A)
# print(half)


def all_sum_patterns(arr):
    patterns = []
    length = len(arr)
    for i in range(1 << length):
        sum = 0
        for j in range(length):
            if i >> j & 1:
                sum += arr[j]
        patterns.append(sum)
    return patterns


# ビット全探索をする？？？
first_half_sum_patterns = all_sum_patterns(first_half_A)
# print(first_half_sum_patterns)

second_half_sum_patterns = all_sum_patterns(second_half_A)
# print(second_half_sum_patterns)
second_half_sum_patterns.sort()

for first_half_sum in first_half_sum_patterns:
    length = len(second_half_sum_patterns)

    def is_ok(index):
        if index < 0:
            return True
        if index >= length:
            return False
        return first_half_sum + second_half_sum_patterns[index] <= K

    ok = -1
    ng = length
    while (ng - ok) > 1:
        mid = (ng + ok) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    if first_half_sum + second_half_sum_patterns[ok] == K:
        print("Yes")
        exit()
print("No")
