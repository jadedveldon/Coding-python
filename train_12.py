n = int(input())
arr = list(map(int, input().strip().split()))[:n]
arrE = []
for i in range(0, n, 2):
    arrE.append(arr[i])
arrE.sort()
j = 0
for i in range(0, n, 2):
    arr[i] = arrE[j]
    j += 1
print(*arr)
