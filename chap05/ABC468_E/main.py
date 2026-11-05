from fractions import Fraction


class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        self.length = len(_list)
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
        if left_index < 0 or self.length <= right_index or right_index < left_index:
            raise
        return self.sum(right_index) - self.sum(left_index - 1)


# 有理数mod
def rational_mod(e: Fraction, mod: int):
    denominator = pow(e.denominator, -1, mod)
    return Fraction(e.numerator * denominator % mod, 1)


N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

if N == 1:
    print(A[0])
    exit()

# a0 + 2a1 + 3a2 + 2a3 + a4
A2: list[int] = []
for i in range(N):
    a = A[i]
    c = min(i, N - 1 - i) + 1
    A2.append(c * a)


cum_sum_a = CumulativeSum(A)
cum_sum_a2 = CumulativeSum(A2)

answer = Fraction(0, 1)
for i in range(N):
    sep1 = min(i, N - i - 1)
    sep2 = N - 1 - sep1
    # print(i, sep1, sep2)
    c = sep1 + 1

    value = cum_sum_a2.range_sum(0, sep1)
    if sep1 + 1 <= sep2 - 1:
        value += cum_sum_a.range_sum(sep1 + 1, sep2 - 1) * c
    if sep1 == sep2:
        value += cum_sum_a2.range_sum(sep2 + 1, N - 1)
    else:
        value += cum_sum_a2.range_sum(sep2, N - 1)

    value = Fraction(value, i + 1)
    answer += value
    answer = rational_mod(answer, MOD)

answer = rational_mod(answer, MOD)
print(answer)
