def neg_bundle():
    n = int(input("Enter the size of the array"))
    arr = list(map(int, input("Enter the numbers : ").strip().split()))[:n]
    neg = []
    for i in arr:
        if i < 0:
            neg.append(i)
    for i in arr:
        if i not in neg:
            neg.append(i)
    print(neg)
neg_bundle()