from typing import List, Any
def rev_arr():
    n = int(input("Enter the size of the array"))
    arr = []
    for i in range(n):
        a = int(input())
        arr.append(a)
    rev = arr[::-1]
    return rev
fin = []
fin = rev_arr()
print(fin)
