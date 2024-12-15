X, Y = map(int, input().split())
if X == 1 and Y == 1:
    print(0)
    exit()


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pairs = [Pair(X, Y)]
while True:
    if X > Y:
        X -= Y
    else:
        Y -= X
    if X == 1 and Y == 1:
        break
    pairs.append(Pair(X, Y))


pairs.reverse()
print(len(pairs))
for pair in pairs:
    print(pair.x, pair.y)
