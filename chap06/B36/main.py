N, K = map(int, input().split())
S = list(input())
# print(S)
on_num = 0
for s in S:
    if s == "1":
        on_num += 1


def is_even(num):
    return num % 2 == 0


if is_even(on_num) == is_even(K):
    print("Yes")
else:
    print("No")
