a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

x = 'a' if a > b and a > c else 'b' if b > a and b > c else 'c'

print(x)
