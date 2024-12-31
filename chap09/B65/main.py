import sys

sys.setrecursionlimit(1000000)


class Employee:
    def __init__(self) -> None:
        self.neighbors: list[Employee] = []
        self.rank = 0
        self.finalized = False


N, T = map(int, input().split())
emploees = [Employee() for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    emploee_1 = emploees[a]
    emploee_2 = emploees[b]
    emploee_1.neighbors.append(emploee_2)
    emploee_2.neighbors.append(emploee_1)

boss = emploees[T - 1]


def calc_rank(emploee: Employee):
    subordinates_max_rank = -1
    emploee.finalized = True
    for neighbor in emploee.neighbors:
        if neighbor.finalized:
            continue
        subordinates_max_rank = max(subordinates_max_rank, calc_rank(neighbor))
    emploee.rank = subordinates_max_rank + 1
    return emploee.rank


calc_rank(boss)

print(" ".join([str(emploee.rank) for emploee in emploees]))
