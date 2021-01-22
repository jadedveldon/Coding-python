def sort012():
    n = int(input('Enter the size of the array:'))
    print("Enter the elements of the array but only values 0 , 1 and 2 are accepted:")
    arr = []
    for i in range(n):
        ele = int(input())
        if ele in range(3):
            arr.append(ele)
        else:
            print("Not acceptable")
    count0 = 0
    count1 = 0
    count2 = 0
    for j in arr:
        if j == 0:
            count0 = count0 + 1
        elif j == 1:
            count1 = count1 + 1
        else:
            count2 = count2 + 1
    newArr = []
    for k in range(count0):
        newArr.append('0')
    for k in range(count1):
        newArr.append('1')
    for k in range(count2):
        newArr.append('2')
    print("The sorted array is:", newArr)
    print(count0,count1,count2)
sort012()
