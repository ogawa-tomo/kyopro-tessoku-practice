# 座標圧縮
class Compress:
    def __init__(self, org_list: list[int]) -> None:
        self.org_list = org_list

        copied = org_list.copy()
        copied = list(set(copied))
        copied.sort()

        # もとの数列の値を与えたとき、何番目に大きい値かを返す辞書
        self.rank_by_num: dict[int, int] = dict()
        for i in range(len(copied)):
            c = copied[i]
            self.rank_by_num[c] = i

        # selc.compressed[i]: もとの数列のi番目が、何番目に大きい値か
        self.compressed: list[int] = []
        for v in self.org_list:
            self.compressed.append(self.rank_by_num[v])


def get_compressed(org_list: list[int]):
    return Compress(org_list).compressed


N = int(input())
A: list[int] = []
for _ in range(N):
    a = int(input())
    A.append(a)

for v in get_compressed(A):
    print(v)
