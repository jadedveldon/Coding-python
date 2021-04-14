s = (2, 3, 4)
ss = (3, 4, 5)
sss = ()
for i in s:
    if i not in ss:
        sss.add(i)
print(sss)
