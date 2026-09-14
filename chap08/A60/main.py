N = int(input())
A = list(map(int, input().split()))


class T:
    def __init__(self, i: int, v: int) -> None:
        self.i = i
        self.v = v

    def __repr__(self) -> str:
        return str((self.i, self.v))


l2: list[T] = []
answer: list[int] = []
for i in range(N):
    a = A[i]
    if i >= 1:
        l2.append(T(i - 1, A[i - 1]))
        while l2:
            if l2[-1].v <= a:
                l2.pop()
            else:
                break
    # print(l2)
    if l2:
        answer.append(l2[-1].i + 1)
    else:
        answer.append(-1)

print(*answer)
