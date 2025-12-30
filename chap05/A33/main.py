N = int(input())
A = list(map(int, input().split()))

xor_sum = 0
for a in A:
    xor_sum ^= a

if xor_sum == 0:
    print("Second")
else:
    print("First")
