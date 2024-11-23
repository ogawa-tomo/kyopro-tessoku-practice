N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = []
R = []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

win = 0
lose = 0
S_win = []
S_lose = []
for a in A:
    if a == 1:
        win += 1
    else:
        lose += 1
    S_win.append(win)
    S_lose.append(lose)
for i in range(Q):
    l = L[i] - 1
    r = R[i] - 1
    if l >= 1:
        win = S_win[r] - S_win[l - 1]
        lose = S_lose[r] - S_lose[l - 1]
    else:
        win = S_win[r]
        lose = S_lose[r]
    if win > lose:
        print("win")
    elif lose > win:
        print("lose")
    else:
        print("draw")
