n = int(input("enter the size of dict:"))
d = {}
for i in range(1,n+1):
    key = i
    value = i ** 2
    d[key] = value
print(d)
