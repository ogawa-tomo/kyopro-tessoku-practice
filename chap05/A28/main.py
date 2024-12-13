N = int(input())
M = 10000

number = 0
for _ in range(N):
    T, A = input().split()
    # print(T, A)
    A = int(A)
    if T == "+":
        number += A
    if T == "-":
        number -= A
    if T == "*":
        number *= A
    number %= M
    if number < 0:
        number += M
    print(number)
