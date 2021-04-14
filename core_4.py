n = int(input("enter the size of dict 1:"))
d = {}
for i in range(n):
    key = int(input("Key"))
    value = int(input("Value"))
    d[key] = value
m = int(input("enter the size of dict 2:"))
di = {}
for i in range(m):
    key = int(input("Key"))
    value = int(input("Value"))
    di[key] = value
d.update(di)
print(d)