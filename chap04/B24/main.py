N = int(input())


class Box:
    def __init__(self, i: int, x: int, y: int):
        self.i = i
        self.x = x
        self.y = y

        # 自身が最も外側にある箱の置き方のうち、最長のものの長さ
        self.max_length = 0

    def __repr__(self):
        return str((self.x, self.y))

    def __lt__(self, other):
        if self.x == other.x:
            # yが大きいほうを前にもってくる必要がある
            return self.y > other.y
        return self.x < other.x


boxes: list[Box] = []

for i in range(N):
    x, y = map(int, input().split())
    box = Box(i, x, y)
    boxes.append(box)

boxes.sort()

# LY[l]: 長さlの箱の重なりの最後の箱として考えられるYの最小値
LY: list[int] = [0]

for box in boxes:
    length = len(LY)

    # ok: 値がbox.y未満であるLのインデックスの最大値
    ok = 0
    ng = length
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if LY[mid] < box.y:
            ok = mid
        else:
            ng = mid

    max_length = ok + 1
    box.max_length = max_length

    if length > max_length:
        LY[max_length] = min(LY[max_length], box.y)
    else:
        LY.append(box.y)

answer = 0
for box in boxes:
    answer = max(answer, box.max_length)

print(answer)
