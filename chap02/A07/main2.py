class Cover:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right


class Coverd1D:
    def __init__(self, covers: list[Cover], length: int):

        # 出席者数の前日比
        x = [0] * (length + 1)
        for cover in covers:
            x[cover.left] += 1
            x[cover.right + 1] -= 1

        # 累積和
        self.coverd: list[int] = []
        total = 0
        for i in range(length):
            total += x[i]
            self.coverd.append(total)


D = int(input())
N = int(input())
# L = []
# R = []
covers: list[Cover] = []
for _ in range(N):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    covers.append(Cover(l, r))

coverd = Coverd1D(covers, D).coverd
for c in coverd:
    print(c)
