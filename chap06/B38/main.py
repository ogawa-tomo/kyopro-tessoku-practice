N = int(input())
S = list(input())
# print(S)

# arr[i]: i番目の草の高さの最小値
arr = [1] * N
i = 0
while i < N - 1:
    # print(i)
    if S[i] == "A":
        arr[i + 1] = arr[i] + 1
        i += 1
    elif S[i] == "B":
        # Bがiからjまで連続する
        j = i
        while j < N - 2 and S[j + 1] == "B":
            j += 1
        # print(j)
        value = 1
        # j + 1からi + 1までは、1, 2, ...と増やす
        for idx in range(j + 1, i, -1):
            arr[idx] = value
            value += 1
        arr[i] = max(arr[i], value)
        i = j + 1

# print(arr)


print(sum(arr))
