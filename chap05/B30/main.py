H, W = map(int, input().split())
n = H + W - 2
r = H - 1

mod = 1000000007


# a^bをmodで割った余りを返す
def mod_power(a, b, mod):
    answer = 1
    while b > 0:
        # i回目のループで、bが2^iの成分を持っていれば、掛け算をする
        if b & 1:
            answer = (answer * a) % mod
        # i回目のループでは、a^(2^i)をかける（0回目: a^1, 1回目: a^2, 2回目: a^4, ...）
        a = a * a % mod
        b >>= 1
    return answer


# aの階乗をmodで割った余りを返す
def fact(a, mod):
    answer = 1
    for i in range(1, a + 1):
        answer *= i
        answer %= mod
    return answer


# nCrをmodで割った余りを返す
def combination(n, r, mod):
    # nの階乗
    n_fact = fact(n, mod)

    # rの階乗
    r_fact = fact(r, mod)
    # n-rの階乗
    n_r_fact = fact(n - r, mod)
    bunshi = r_fact * n_r_fact % mod

    return (n_fact * mod_power(bunshi, mod - 2, mod)) % mod


print(combination(n, r, mod))
