N, Q = map(int, input().split())
arr = list(range(1, N + 1))
# print(arr)
reverse = False
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        y = int(query[2])
        x -= 1
        if reverse:
            x = N - 1 - x
        arr[x] = y
    elif query[0] == "2":
        reverse = not reverse
    elif query[0] == "3":
        x = int(query[1])
        x -= 1
        if reverse:
            x = N - 1 - x
        print(arr[x])
