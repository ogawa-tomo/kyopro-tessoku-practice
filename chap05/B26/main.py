import math

N = int(input())

# class Number:
#     def __init__(self, value):
#         self.value = value
#         self.is_prime = None # None or True or False

# numbers = []
# for i in range(1, N + 1):
#     numbers.append(Number(i))

# is_prime_arr[i]: iが素数ならTrue、合成数ならFalse
is_prime_arr = [True] * (N + 1)
is_prime_arr[0] = False
is_prime_arr[1] = False


for i in range(2, math.ceil(math.sqrt(N))):
    if not is_prime_arr[i]:
        continue
    for j in range(2 * i, N + 1, i):
        is_prime_arr[j] = False

# print(is_prime_arr)
for i in range(2, N + 1):
    if is_prime_arr[i]:
        print(i)
