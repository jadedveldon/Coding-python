n = int(input())
arr = list(map(int, input().strip().split()))[:n]
sums = sum(arr)
if sums % 2 == 0:
    if sums % 3 == 0:
        if sums % 5 == 0:
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    print(0)
