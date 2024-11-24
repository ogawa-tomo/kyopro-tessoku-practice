N, K = map(int, input().split())
A = list(map(int, input().split()))

# print(10 // 3)


# t秒後の時点で出力されているチラシの枚数
def output(t):
    total = 0
    for a in A:
        total += t // a
    return total


min = 1
max = 1000000000
while min < max:
    t = int((min + max) / 2)
    num = output(t)
    if num < K:
        min = t + 1
    else:
        max = t
print(max)


#     if num == K:
#         print(t)
#         exit()
#     if num > K:
#         max = t
#     if num < K:
#         min = t
#     if max == min + 1:
#         break
# print(max)
