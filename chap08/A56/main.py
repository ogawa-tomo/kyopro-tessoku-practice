N, Q = map(int, input().split())
S = input()
mod = 2147483647
# print(ord("a"))
T = [ord(s) - ord("a") + 1 for s in S]
# print(T)
Power100 = [1] * N
for i in range(1, N):
    Power100[i] = 100 * Power100[i - 1] % mod

# print(Power100)

H: list[int] = [0] * N
for i in range(N):
    if i == 0:
        H[i] = T[i]
        continue
    H[i] = (100 * H[i - 1] + T[i]) % mod

# print(H[-1])
# print(H)


def hash(l: int, r: int):
    if l == 0:
        return H[r]
    value = H[r] - (H[l - 1] * Power100[r - l + 1] % mod)
    if value < 0:
        value += mod
    return value


for _ in range(Q):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    # print(hash(a, b))
    # print(hash(c, d))
    if hash(a, b) == hash(c, d):
        print("Yes")
    else:
        print("No")
