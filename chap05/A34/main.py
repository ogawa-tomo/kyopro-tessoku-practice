N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

# grundy[i]: 石がi個のときのgrundy数
grundy: list[int] = [0] * (10**5 + 1)
for i in range(10**5 + 1):
    # transit[i]: grundy数がiとなるような遷移ができるか
    transit: list[int] = [False] * 3
    if i >= X:
        transit[grundy[i - X]] = True
    if i >= Y:
        transit[grundy[i - Y]] = True
    if not transit[0]:
        grundy[i] = 0
    elif not transit[1]:
        grundy[i] = 1
    else:
        grundy[i] = 2
# print(grundy)
xor_sum = 0
for a in A:
    xor_sum ^= grundy[a]

if xor_sum != 0:
    print("First")
else:
    print("Second")
