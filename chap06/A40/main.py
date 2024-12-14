import math

N = int(input())
A = list(map(int, input().split()))
# print(A)


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# arr[i]: 長さiの棒の本数
arr = [0] * 101
for a in A:
    arr[a] += 1
# print(arr)

answer = 0
for num in arr:
    if num < 3:
        continue
    answer += comb(num, 3)
print(answer)
