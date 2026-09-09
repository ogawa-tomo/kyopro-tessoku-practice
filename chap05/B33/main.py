N, H, W = map(int, input().split())
xor_sum = 0
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    xor_sum ^= a
    xor_sum ^= b

if xor_sum == 0:
    print("Second")
else:
    print("First")
