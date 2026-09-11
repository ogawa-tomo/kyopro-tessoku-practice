class Hash:
    def __init__(self, S: str) -> None:
        self.mod = 2147483647
        t = [ord(s) for s in S]
        self.b = [1] * len(S)
        for i in range(1, len(S)):
            self.b[i] = 100 * self.b[i - 1] % self.mod
        self.h = [0] * len(S)
        self.h[0] = t[0]
        for i in range(1, len(S)):
            self.h[i] = (100 * self.h[i - 1] + t[i]) % self.mod

    def hash(self, l: int, r: int):
        if l == 0:
            return self.h[r]
        value = self.h[r] - self.h[l - 1] * self.b[r - l + 1]
        return value % self.mod


N, Q = map(int, input().split())
# S = list(input())
S = list(input())
S2 = list(reversed(S))
# print(S)
# print(S2)
hash = Hash("".join(S))
hash2 = Hash("".join(S2))
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    l2 = N - 1 - r
    r2 = N - 1 - l
    if hash.hash(l, r) == hash2.hash(l2, r2):
        print("Yes")
    else:
        print("No")
