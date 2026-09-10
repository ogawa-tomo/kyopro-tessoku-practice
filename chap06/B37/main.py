N = int(input())
digits = len(str(N))
# print(digits)

answer = 0
for digit in range(digits):
    for i in range(10):
        # 右からdigit桁目の数字がiである数が、N以下にいくつあるか
        num = 0

        # 右からdigit桁目の数
        d = int(str(N)[digits - 1 - digit])

        if i < d:
            num = (N // (10 ** (digit + 1)) + 1) * 10**digit
        elif i > d:
            num = (N // (10 ** (digit + 1))) * 10**digit
        else:
            num = (N // (10 ** (digit + 1))) * 10**digit + N % 10**digit + 1

        answer += num * i

print(answer)
