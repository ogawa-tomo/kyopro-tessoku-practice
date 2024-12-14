N = int(input())
A = list(map(int, input().split()))

# cnt[i]: 100で割った余りがiである数の個数
cnt = [0] * 100
for a in A:
    amari = a % 100
    cnt[amari] += 1
# print(cnt)

answer = 0
if cnt[0] >= 2:
    answer += cnt[0] * (cnt[0] - 1) // 2
if cnt[50] >= 2:
    answer += cnt[50] * (cnt[50] - 1) // 2

for i in range(1, 50):
    j = 100 - i
    answer += cnt[i] * cnt[j]
print(answer)
