N, A, B = map(int, input().split())

# arr[i]: i個の石で始まったとき、先手が勝つか
arr = []
for i in range(N + 1):
    if i - A >= 0 and not arr[i - A]:
        arr.append(True)
        continue
    if i - B >= 0 and not arr[i - B]:
        arr.append(True)
        continue
    arr.append(False)
# print(arr)
# print(arr[N])
if arr[N]:
    print("First")
else:
    print("Second")
