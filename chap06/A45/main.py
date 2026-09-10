N, C = input().split()
A = input()

color_score = {
    "W": 0,
    "B": 1,
    "R": 2,
}

score = 0
for a in A:
    score += color_score[a]

if score % 3 == color_score[C]:
    print("Yes")
else:
    print("No")
