class Hash:
    def __init__(self, S: str) -> None:
        self.mod = 2147483647
        self.s = S
        self.t = [ord(s) for s in self.s]
        self.b = [1] * len(S)
        for i in range(1, len(S)):
            self.b[i] = 100 * self.b[i - 1] % self.mod
        self.h = [0] * len(S)
        self.h[0] = self.t[0]
        for i in range(1, len(S)):
            self.h[i] = (100 * self.h[i - 1] + self.t[i]) % self.mod

    def hash(self, l: int, r: int):
        if l == 0:
            return self.h[r]
        value = self.h[r] - self.h[l - 1] * self.b[r - l + 1]
        return value % self.mod


N, Q = map(int, input().split())
S = input()

hash = Hash(S)
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if hash.hash(a, b) == hash.hash(c, d):
        print("Yes")
    else:
        print("No")
