n = int(input())
arr = list(map(int, input().strip().split()))[:n]
minis = []
final = []
for i in arr:
    mini = arr.count(i)
    minis.append(mini)
mini = min(minis)
for i in range(n):
    if minis[i] == mini:
        if arr[i] not in final:
            final.append(arr[i])
final.sort()
final.reverse()
print(*final)

