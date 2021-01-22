def intuni():
    n = int(input("Enter size of array 1:"))
    m = int(input("Enter size of array 2:"))
    arr1 = list(map(int, input("Enter the elements of list 1:").strip().split()))[:n]
    arr2 = list(map(int, input("Enter the elements of list 2:").strip().split()))[:m]
    union = []
    for i in arr1:
        union.append(i)
    for i in arr2:
        if i not in arr1:
            union.append(i)
    intersection = []
    for j in arr1:
        if j in arr2:
            intersection.append(j)
    print("The union of 2 arrays is:",union)
    print('The intersection of 2 arrays is:',intersection)
intuni()