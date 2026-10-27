N = int(input())


# x以下の素数列挙
def sieve_of_eratosthenes(x: int):
    nums = [i for i in range(x + 1)]

    root = int(pow(x, 0.5))
    for i in range(2, root + 1):
        if nums[i] != 0:
            for j in range(i, x + 1):
                if i * j >= x + 1:
                    break
                nums[i * j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


primes = sieve_of_eratosthenes(1000000)
answer = 0
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        p = primes[i]
        q = primes[j]
        n = p * q**3
        if n > N:
            break
        # print(p, q)
        answer += 1

print(answer)
