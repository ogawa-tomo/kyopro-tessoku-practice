class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        total = 0
        self.cumulative_sum_list: list[int] = []
        for elem in self._list:
            total += elem
            self.cumulative_sum_list.append(total)

    def sum(self, index: int):
        if index == -1:
            return 0
        return self.cumulative_sum_list[index]

    def range_sum(self, left_index: int, right_index: int):
        return self.sum(right_index) - self.sum(left_index - 1)


class Monster:
    def __init__(self, i: int, x: int, y: int):
        self.i = i
        self.x = x
        self.y = y
        self.angle_index = 0  # 何番目に小さい角度か

    @property
    def is_upper(self):
        # 上半平面(0<=degree<180)かどうか
        return self.y > 0 or (self.y == 0 and self.x > 0)

    def __lt__(self, other):
        # 偏角ソート
        if self.is_upper and not other.is_upper:
            return True
        elif (not self.is_upper) and other.is_upper:
            return False
        return cross(self, other) > 0

    def __repr__(self):
        return str(self.i)


def cross(monster1: Monster, monster2: Monster):
    return monster1.x * monster2.y - monster1.y * monster2.x


def equals(monster1: Monster, monster2: Monster):
    if monster1.is_upper != monster2.is_upper:
        return False
    # print("hoge")
    return cross(monster1, monster2) == 0


N, Q = map(int, input().split())

monsters: list[Monster] = []
for i in range(N):
    x, y = map(int, input().split())

    monster = Monster(i, x, y)
    monsters.append(monster)


sorted_monsters = sorted(monsters, reverse=True)

# monster_num[index]: index番目に小さい角度にmonsterが何匹いるか
monster_num: list[int] = []
current_index = 0
for i in range(N):
    monster = sorted_monsters[i]
    if i == 0:
        monster_num.append(1)
        monster.angle_index = current_index
        continue
    prev_monster = sorted_monsters[i - 1]
    if equals(prev_monster, monster):
        monster_num[current_index] += 1
        monster.angle_index = current_index
    else:
        monster_num.append(1)
        current_index += 1
        monster.angle_index = current_index


cum_sum = CumulativeSum(monster_num)
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    monster_a = monsters[a]
    monster_b = monsters[b]

    a_index = monster_a.angle_index
    b_index = monster_b.angle_index
    # print(a_index, b_index)

    if a_index <= b_index:
        print(cum_sum.range_sum(a_index, b_index))
    else:
        answer = cum_sum.range_sum(a_index, len(monster_num) - 1)
        answer += cum_sum.range_sum(0, b_index)
        print(answer)
