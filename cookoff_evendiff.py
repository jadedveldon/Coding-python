t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    even = 0
    odd = 0
    for j in arr:
        if j % 2 == 0:
            even += 1
        else:
            odd += 1
    if even < odd:
        print(n - odd)
    else:
        print(n - even)
