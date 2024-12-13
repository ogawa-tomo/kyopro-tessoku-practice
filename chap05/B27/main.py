A, B = map(int, input().split())


def GCD(A, B):

    while A > 0 and B > 0:
        if A > B:
            A = A % B
        else:
            B = B % A

    if A == 0:
        return B
    else:
        return A


print((A * int(B / GCD(A, B))))
