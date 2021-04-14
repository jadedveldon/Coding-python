n = int(input())
arr = list(map(int, input().strip().split()))[:n]
minis = []
for i in arr:
    mini = arr.count(i)
    minis.append(mini)
for i in range(n):
    if minis[i] == 2:
        result = arr[i]
print(result)