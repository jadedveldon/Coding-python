def ceil(n):
    return int(-1 * n // 1 * -1)
t = int(input())
for i in range(t):
    n, k = input().split()
    n = int(n)
    k = int(k)
    arr = list(map(int, input().strip().split()))[:n]
    arr.sort()
    ans = []
    for o in arr:
        if o >= 0:
            ans.append(o)
    m = len(ans)
    n_o = ceil(n/2)
    if m < n_o:
        print("Rejected")
    elif arr[n-1] > k:
        print("Too slow")
    elif (m == n) and (arr[n-1] == 1):
        print("Bot")
    else:
        print("Accepted")