D, N = map(int, input().split())

# arr[i]: i日目に働く時間
arr = [24] * D

for _ in range(N):
    L, R, H = map(int, input().split())
    L -= 1
    R -= 1
    for i in range(L, R + 1):
        if arr[i] > H:
            arr[i] = H

# print(arr)
print(sum(arr))
