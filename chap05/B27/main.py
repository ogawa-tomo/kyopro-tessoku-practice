A, B = map(int, input().split())


def GCD(A: int, B: int):

    while A > 0 and B > 0:
        if A > B:
            A = A % B
        else:
            B = B % A

    if A == 0:
        return B
    else:
        return A


def LCM(A: int, B: int):
    return A * int(B / GCD(A, B))


print(LCM(A, B))
