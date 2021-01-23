def cyclic_array():
    n = int(input("Enter the size of the array:"))
    arr = list(map(int, input("Enter the elements of the list:").strip().split()))[:n]
    fin = []
    i = arr[n-1]
    fin.append(i)
    for i in range(n-1):
        j = arr[i]
        fin.append(j)
    print(fin)
cyclic_array()