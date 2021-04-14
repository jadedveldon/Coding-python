n,m = input().split()
n = int(n)
m = int(m)
arr = list(map(int, input().strip().split()))[:n]
var = -1
for i in range(n):
    if arr[i] == m:
        var = i

print(var)