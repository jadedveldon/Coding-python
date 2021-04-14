n = int(input("enter the size of dict:"))
d = {}
for i in range(n):
    key = int(input("Key"))
    value = int(input("Value"))
    d[key] = value
a = int(input("Enter the key value to be checked"))
c = 0
for i in d.keys():
    if a == i:
        c = 1
if c == 1:
    print("Exists")
else:
    print("Doesn't exist")