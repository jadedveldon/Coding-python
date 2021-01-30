t = int(input())
for i in range(t):
    arr = list(map(int, input().strip().split()))[:3]
    arr.sort()
    sums = arr[0] + arr[1]
    if sums == arr[2]:
        print("YES")
    else:
        print("NO")
