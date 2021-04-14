n = int(input("enter the size of dict:"))
d = {}
for i in range(n):
    key = int(input("Key"))
    value = int(input("Value"))
    d[key] = value
print(d)