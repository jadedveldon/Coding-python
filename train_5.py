phy = int(input("Enter marks for Physics:"))
chem = int(input("Enter marks for Chemistry:"))
bio = int(input("Enter marks for Biology:"))
math = int(input("Enter marks for Mathematics:"))
comp = int(input("Enter marks for Computers:"))

overall = (phy+chem+bio+math+comp)/5

if overall >= 90:
    grade = 'A'
elif overall >= 80:
    grade = 'B'
elif overall >= 70:
    grade = 'C'
elif overall >= 60:
    grade = 'D'
elif overall >= 40:
    grade = 'E'
else:
    grade = 'F'

print(overall)
print(grade)

