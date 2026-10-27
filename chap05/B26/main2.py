import math


# x以下の素数列挙
def sieve_of_eratosthenes(x: int):
    nums = [i for i in range(x + 1)]

    root = math.isqrt(x)
    for i in range(2, root + 1):
        if nums[i] != 0:
            for j in range(i, x + 1):
                if i * j >= x + 1:
                    break
                nums[i * j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


N = int(input())

for prime in sieve_of_eratosthenes(N):
    print(prime)
