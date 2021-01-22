def kminmax():
    n = int(input("Enter the size of the array:"))
    print('Enter the elements')
    arr = []
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    k = int(input("Enter the Kth value to find min max:"))
    arr.sort()
    uniqArr = []
    for j in arr:
        if j not in uniqArr:
            uniqArr.append(j)
    Kthmin = uniqArr[k-1]
    Kthmax = uniqArr[n-k]
    print('The Kth minimum element is: ',Kthmin)
    print('The Kth maximum element is: ', Kthmax)
kminmax()
