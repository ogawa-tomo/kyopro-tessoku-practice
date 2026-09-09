N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


# 石がi個のときのGrundy数
def grundy(i: int):
    amari = i % 5
    match amari:
        case 0 | 1:
            return 0
        case 2 | 3:
            return 1
        case _:
            return 2


xor_sum = 0
for a in A:
    xor_sum ^= grundy(a)

if xor_sum != 0:
    print("First")
else:
    print("Second")
