from typing import Callable


# 単調増加関数func(x)が与えられたとき、
# min_left <= x <= min_right のなかで、
# func(x) = target となるようなxを、
# 誤差epsilonで求める
def find_real_number(
    min_left: float,
    max_right: float,
    func: Callable[[float], float],
    target: float,
    epsilon: float,
):
    if target < func(min_left) or func(max_right) < target:
        raise
    left = min_left
    right = max_right

    mid = (right + left) / 2
    while right - left > epsilon:
        mid = (right + left) / 2
        if func(mid) < target:
            left = mid
        else:
            right = mid

    return mid


def func(x: float):
    return x**3 + x


N = int(input())
left = 0
right = 100

print(find_real_number(0, 100, func, N, 0.001))
