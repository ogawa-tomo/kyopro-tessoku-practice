def func(x):
    return x**3 + x


N = int(input())
min = 0
max = 100

while max - min > 0.001:
    mid = (max + min) / 2
    y = func(mid)
    if N > y:
        min = mid
    else:
        max = mid

print(mid)
