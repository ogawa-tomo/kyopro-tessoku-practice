N = int(input())

# d[num]: 値がnumであるデータの個数
d: dict[int, int] = {}
for _ in range(N):
    value = int(input())
    if value in d:
        d[value] += 1
    else:
        d[value] = 1

# print(d)
answer = 0
for num in d.values():
    # print(num)
    answer += num * (num - 1) // 2
print(answer)
