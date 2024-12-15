N, M = map(int, input().split())
A = list(map(int, input().split()))

# arr[i]: i番目の生徒の不正解数
arr = [0] * N
for a in A:
    a -= 1
    arr[a] += 1

for a in arr:
    print(M - a)
