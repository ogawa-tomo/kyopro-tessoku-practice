import math


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


Q = int(input())
for _ in range(Q):
    x = int(input())
    if is_prime(x):
        print("Yes")
    else:
        print("No")
