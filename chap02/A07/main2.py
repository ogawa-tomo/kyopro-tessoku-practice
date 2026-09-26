class Cover:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right


# 座標ごとに覆われている数のリストを返す
def covered(covers: list[Cover], length: int):
    # 出席者数の前日比
    x = [0] * (length + 1)
    for cover in covers:
        x[cover.left] += 1
        x[cover.right + 1] -= 1

    # 累積和
    covered_list: list[int] = []
    total = 0
    for i in range(length):
        total += x[i]
        covered_list.append(total)

    return covered_list


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


for c in covered(covers, D):
    print(c)
