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


N, Q = map(int, input().split())
A = list(map(int, input().split()))

cumulative_sum = CumulativeSum(A)
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(cumulative_sum.range_sum(l, r))
