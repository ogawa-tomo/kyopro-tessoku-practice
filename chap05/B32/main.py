N, K = map(int, input().split())
A = list(map(int, input().split()))

# arr[i]: i個の状態で開始したとき、先手が勝つか
arr = []
for i in range(N + 1):
    answer = False
    for a in A:
        if i - a >= 0 and not arr[i - a]:
            answer = True
            break
    arr.append(answer)
if arr[N]:
    print("First")
else:
    print("Second")
