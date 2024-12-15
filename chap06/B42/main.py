N = int(input())


class Card:
    def __init__(self, omote, ura):
        self.omote = omote
        self.ura = ura


class CardList(list[Card]):
    def score(self):
        omote_score = 0
        ura_score = 0
        for card in self:
            omote_score += card.omote
            ura_score += card.ura
        return abs(omote_score) + abs(ura_score)


cards = CardList()
for _ in range(N):
    omote, ura = map(int, input().split())
    cards.append(Card(omote, ura))

answer = 0

# 表も裏も正が基準
selected = CardList()
for card in cards:
    if card.omote + card.ura > 0:
        selected.append(card)
answer = max(answer, selected.score())


# 表が正で裏が負が基準
selected = CardList()
for card in cards:
    if card.omote - card.ura > 0:
        selected.append(card)
answer = max(answer, selected.score())

# 表が負で裏が正
selected = CardList()
for card in cards:
    if -card.omote + card.ura > 0:
        selected.append(card)
answer = max(answer, selected.score())

# 表も裏も負
selected = CardList()
for card in cards:
    if -card.omote - card.ura > 0:
        selected.append(card)
answer = max(answer, selected.score())

print(answer)
