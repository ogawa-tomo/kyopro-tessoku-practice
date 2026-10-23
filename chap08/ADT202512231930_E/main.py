from functools import cache
import math
from fractions import Fraction


N = int(input())

# これだと、@lru_cacheしたときに答えが変わってしまう
# class Calc:
#     def __init__(self):
#         self.answer = 0

#     def calc(self, n: int):
#         if n <= 1:
#             return
#         self.answer += n
#         ceil = math.ceil(n / 2)
#         floor = math.floor(n / 2)
#         self.calc(ceil)
#         self.calc(floor)


# calc = Calc()
# calc.calc(N)
# print(calc.answer)

# answer = 0


# lru_cacheよりこっちのが楽
@cache
def calc(n: int):
    if n <= 1:
        return 0
    half = Fraction(n, 2)
    ceil = math.ceil(half)
    floor = math.floor(half)
    return n + calc(ceil) + calc(floor)


print(calc(N))
