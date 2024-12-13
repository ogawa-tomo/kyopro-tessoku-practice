a, b = map(int, input().split())
mod = 1000000007

answer = 1
while b > 0:
    # i回目のループで、bが2^iの成分を持っていれば、掛け算をする
    if b & 1:
        answer = (answer * a) % mod
    # i回目のループでは、a^(2^i)をかける（0回目: a^1, 1回目: a^2, 2回目: a^4, ...）
    a = a * a % mod
    b >>= 1
print(answer)
