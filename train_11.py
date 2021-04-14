n = int(input())
arr = list(map(float, input().strip().split()))[:n]
arr.sort()
mini = arr[1] - arr[0]
for i in range(n - 1):
    mini1 = arr[i + 1] - arr[i]
    if mini1 < mini:
        mini = mini1
        a = arr[i + 1]
        b = arr[i]
print(a)
print(b)
# 138.3 156.5 156.6 160.2 198.3 146.2
