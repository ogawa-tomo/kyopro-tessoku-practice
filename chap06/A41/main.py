N = int(input())
S = list(input())
# print(S)

for i in range(N - 2):
    if S[i] == S[i + 1] and S[i] == S[i + 2]:
        print("Yes")
        exit()

print("No")
