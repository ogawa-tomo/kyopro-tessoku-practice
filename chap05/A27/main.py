A, B = map(int, input().split())

while A > 0 and B > 0:
    if A > B:
        A = A % B
    else:
        B = B % A

if A == 0:
    print(B)
else:
    print(A)
