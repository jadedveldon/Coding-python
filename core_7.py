d = {1: 10, 2: 20, 3: 30}
di = {3: 30, 4: 40}
for i in list(d):
    for j in list(di):
        if i == j:
            d[i] = d[i] + di[i]
            del di[i]
d.update(di)
print(d)
