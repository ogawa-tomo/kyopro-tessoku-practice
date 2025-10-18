class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        total = 0
        self.cumulative_sum_list: list[int] = []
        for elem in self._list:
            total += elem
            self.cumulative_sum_list.append(total)

    def sum(self, index: int):
        if index == -1:
            return 0
        return self.cumulative_sum_list[index]

    def range_sum(self, left_index: int, right_index: int):
        return self.sum(right_index) - self.sum(left_index - 1)


N = int(input())
A = list(map(int, input().split()))

hazure = [a ^ 1 for a in A]
atari_cumulative_sum = CumulativeSum(A)
hazure_cumulative_sum = CumulativeSum(hazure)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    atari_num = atari_cumulative_sum.range_sum(l, r)
    hazure_num = hazure_cumulative_sum.range_sum(l, r)
    if atari_num > hazure_num:
        print("win")
    elif atari_num < hazure_num:
        print("lose")
    else:
        print("draw")
