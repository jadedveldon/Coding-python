def largest_subArray():
    n = int(input("Enter the size of the array:"))
    arr = list(map(int, input("Enter elements:").strip().split()))[:n]
    max = arr[0]
    for i in range(n):
        current = 0
        for j in range(i, n):
            current = current + arr[j]
            if current > max:
                max = current
    print(max)
largest_subArray()