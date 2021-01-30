t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    sum = 0
    for j in arr:
        sum += j
    if sum%2 == 0:
        print(1)
    else:
        print(2)