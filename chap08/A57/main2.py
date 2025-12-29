class Doubling:
    def __init__(self, transition_list: list[int], max_digit=30):
        # self.transition_list[i]: iが次に動く場所
        self.transition_list = transition_list
        self.max_digit = max_digit

        self.dp: list[list[int]] = []
        for _ in range(max_digit):
            self.dp.append([0] * len(self.transition_list))
        self.dp[0] = self.transition_list
        for i in range(1, max_digit):
            for j in range(len(self.transition_list)):
                self.dp[i][j] = self.dp[i - 1][self.dp[i - 1][j]]

    # 初期位置がinitのとき、after回後にいる場所
    def result(self, init: int, after: int):
        current = init
        for k in range(self.max_digit, -1, -1):
            if after & (1 << k):
                current = self.dp[k][current]
        return current


N, Q = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] -= 1

doubling = Doubling(A)

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    print(doubling.result(x, y) + 1)
