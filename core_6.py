arr = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))
d = {}
for i in range(len(arr)):
    d[arr[i]] = arr2[i]
print(d)