from typing import Union


class Employee:
    def __init__(self) -> None:
        self.boss: Union[None, Employee] = None
        self.subordinates: list[Employee] = []
        self.num_subordinate = 0


N = int(input())
A = list(map(int, input().split()))
emploees: list[Employee] = [Employee()]
for a in A:
    boss_index = a - 1
    emploee = Employee()
    emploees.append(emploee)
    emploee.boss = emploees[boss_index]
    emploee.boss.subordinates.append(emploee)


for emploee in reversed(emploees):
    for subordinate in emploee.subordinates:
        emploee.num_subordinate += subordinate.num_subordinate + 1

print(" ".join([str(emploee.num_subordinate) for emploee in emploees]))
