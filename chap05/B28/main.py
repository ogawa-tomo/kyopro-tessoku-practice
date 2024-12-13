N = int(input())
mod = 1000000007

arr = []
arr.append(1)
arr.append(1)
for i in range(2, N):
    value = (arr[i - 2] + arr[i - 1]) % mod
    arr.append(value)

print(arr[N - 1])
