n = int(input("Enter range:"))
x = 0
y = 1
print(x)
print(y)
for i in range(n-2):
    z = x+y
    x = y
    y = z
    print(z)
