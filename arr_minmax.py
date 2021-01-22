def minmax():
    n = int(input("Enter the size array:"))
    arr = []
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    arr.sort()
    min = arr[0]
    max = arr[n-1]
    print("min =", min)
    print("max =", max)
minmax()