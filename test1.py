a = []
b = []
final = []
n = int(input())
arr = list(map(int, input().strip().split()))[:n]
for i in arr:
    a.append(i)
arr.reverse()
for i in arr:
    b.append(i)
while len(a) != 0 and len(b) != 0:
    A = a[0]
    B = b[0]
    if A > B:
        print(A,B)
        final.append(1)
        b.remove(B)
    elif A < B:
        print(A,B)
        final.append(2)
        a.remove(A)
    elif A == B:
        print(A,B)
        final.append(0)
        b.remove(B)
        a.remove(A)
print(final)
